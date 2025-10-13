# Simple satellite plotter with real Earth map - plot_satellite.py
import matplotlib.pyplot as plt
import numpy as np
import math
from datetime import datetime, timezone
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from skyfield.api import load, EarthSatellite
from skyfield.timelib import Time

print("Satellite Orbit Plotter (with Real Earth Map)")
print("=" * 50)

# Read the satellite file and find the ISS
print("Looking for ISS in satellite data...")

try:
    with open("satellites.txt", "r") as file:
        lines = file.readlines()
    print("Satellite data loaded!")
except FileNotFoundError:
    print("Error: satellites.txt file not found!")
    print("Make sure you copied it from step 1")
    exit()

# Find the ISS TLE data
iss_name = None
iss_line1 = None
iss_line2 = None

for i in range(len(lines) - 2):
    if "ISS" in lines[i].upper() and "ZARYA" in lines[i].upper():
        # Look for the next two lines that start with "1" and "2"
        for j in range(i + 1, min(i + 5, len(lines))):
            if lines[j].strip().startswith("1 "):
                iss_line1 = lines[j].strip()
            elif lines[j].strip().startswith("2 "):
                iss_line2 = lines[j].strip()
                break
        
        if iss_line1 and iss_line2:
            iss_name = lines[i].strip()
            break

if not iss_name:
    print("Could not find ISS in the data!")
    exit()

print(f"Found: {iss_name}")

# Create ISS satellite object using Skyfield
ts = load.timescale()
satellite = EarthSatellite(iss_line1, iss_line2, iss_name, ts)

# Get basic orbital information from the TLE
inclination_deg = satellite.model.inclo * 180/math.pi
mean_motion_per_day = satellite.model.no_kozai * 1440 / (2 * math.pi)  # Convert to revs per day
orbital_period_hours = 24.0 / mean_motion_per_day

print(f"ISS Orbital Data:")
print(f"   Inclination: {inclination_deg:.1f} degrees")
print(f"   Period: {orbital_period_hours * 60:.1f} minutes")

# Calculate altitude from the satellite's mean motion
earth_radius = 6371  # km
earth_mu = 398600.4418  # Earth's gravitational parameter (km³/s²)
orbital_period_seconds = orbital_period_hours * 3600
mean_motion_rad_per_sec = (2 * math.pi) / orbital_period_seconds
semi_major_axis = (earth_mu / (mean_motion_rad_per_sec ** 2)) ** (1/3)
altitude = semi_major_axis - earth_radius

print(f"   Mean Motion: {mean_motion_per_day:.2f} orbits/day")
print(f"   Semi-major axis: {semi_major_axis:.0f} km")
print(f"   Altitude: {altitude:.0f} km")

# Create the plot with real Earth map using Cartopy
fig, ax = plt.subplots(1, 1, figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
ax.add_feature(cfeature.OCEAN, color='lightblue')
ax.add_feature(cfeature.LAND, color='lightgreen')
ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
ax.add_feature(cfeature.BORDERS, linewidth=0.5, alpha=0.7)
ax.set_global()
ax.gridlines(draw_labels=True, alpha=0.5)

# Generate accurate ISS orbit path and position using Skyfield

# Get current time and generate orbit trace for the next orbital period
current_time = ts.now()
orbit_duration_hours = orbital_period_hours
num_points = 150

# Create time range for one orbit
time_range = ts.tt_jd(current_time.tt + np.linspace(0, orbit_duration_hours/24, num_points))

# Get satellite positions over the orbit
orbit_positions = satellite.at(time_range)
orbit_subpoints = orbit_positions.subpoint()

# Extract latitude and longitude arrays
orbit_lats = orbit_subpoints.latitude.degrees
orbit_lons = orbit_subpoints.longitude.degrees

# Handle longitude discontinuities at ±180° (date line crossings)
def plot_orbit_with_dateline_handling(ax, lons, lats, **kwargs):
    """Plot orbit path while handling dateline crossings properly"""
    # Find large jumps in longitude (> 180 degrees) which indicate dateline crossings
    lon_diffs = np.diff(lons)
    discontinuity_indices = np.where(np.abs(lon_diffs) > 180)[0]
    
    if len(discontinuity_indices) == 0:
        # No dateline crossings, plot normally
        ax.plot(lons, lats, **kwargs)
    else:
        # Plot segments between discontinuities
        start_idx = 0
        for disc_idx in discontinuity_indices:
            # Plot segment up to discontinuity
            segment_lons = lons[start_idx:disc_idx+1]
            segment_lats = lats[start_idx:disc_idx+1]
            ax.plot(segment_lons, segment_lats, **kwargs)
            start_idx = disc_idx + 1
            # Remove label after first segment to avoid duplicate legend entries
            if 'label' in kwargs:
                kwargs = dict(kwargs)
                del kwargs['label']
        
        # Plot final segment
        if start_idx < len(lons):
            segment_lons = lons[start_idx:]
            segment_lats = lats[start_idx:]
            ax.plot(segment_lons, segment_lats, **kwargs)

# Plot the ISS orbit path with proper dateline handling
plot_orbit_with_dateline_handling(ax, orbit_lons, orbit_lats, 
                                color='red', linewidth=2, 
                                label=f'{iss_name} Orbit', alpha=0.9)

# Calculate current ISS position using Skyfield
current_position = satellite.at(current_time)
current_subpoint = current_position.subpoint()
current_lat = current_subpoint.latitude.degrees
current_lon = current_subpoint.longitude.degrees
current_altitude_km = current_subpoint.elevation.km

# Plot current ISS position
ax.plot(current_lon, current_lat, 'ro', markersize=12, label='Current ISS Position', markeredgecolor='white', markeredgewidth=2)

# Add ISS label
ax.annotate('ISS CURRENT POSITION', 
            xy=(current_lon, current_lat), 
            xytext=(current_lon + 20, current_lat + 10),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=11, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.8))

# Set up the plot
ax.set_xlabel('Longitude (degrees)', fontsize=12)
ax.set_ylabel('Latitude (degrees)', fontsize=12)
ax.set_title(f'{iss_name} Orbit Over Earth\n'
            f'Inclination: {inclination_deg:.1f} deg, Altitude: {altitude:.0f}km, Period: {orbital_period_hours:.1f}h', 
            fontsize=14, fontweight='bold')

# Add legend
ax.legend(loc='upper right', fontsize=10)

# Add equator line and basic labels
ax.axhline(y=0, color='red', linestyle='--', alpha=0.5, linewidth=1)
ax.text(0, -5, 'Equator', ha='center', va='top', fontweight='bold', 
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))

print(f"\nCreating world map plot...")
plt.tight_layout()

# Save the plot
plt.savefig('iss_orbit_world_map.png', dpi=300, bbox_inches='tight')
print("Saved plot as 'iss_orbit_world_map.png'")

# Show the plot
plt.show()

print(f"\nSuccess! ISS orbit visualized over real Earth map")
print(f"The ISS passes over most populated areas due to its {inclination_deg:.1f} degree inclination")
print(f"Current position: {current_lat:.1f} deg N, {current_lon:.1f} deg E")
print(f"Current altitude: {current_altitude_km:.0f} km")
print(f"Orbital period: {orbital_period_hours:.1f} hours")