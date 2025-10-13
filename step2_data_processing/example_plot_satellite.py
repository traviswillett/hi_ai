# Simple satellite orbit plotter - visualize the ISS orbit around Earth
import matplotlib.pyplot as plt
import numpy as np
import math

print("🛰️  Satellite Orbit Plotter")
print("=" * 30)

# Read the satellite file and find the ISS
print("📂 Looking for ISS in satellite data...")

try:
    with open("satellites.txt", "r") as file:
        lines = file.readlines()
    print("✅ Satellite data loaded!")
except FileNotFoundError:
    print("❌ Error: satellites.txt file not found!")
    print("💡 Make sure you copied it from step 1")
    exit()

# Find the ISS
iss_data = None
for i in range(len(lines) - 2):
    if "ISS" in lines[i].upper() and "ZARYA" in lines[i].upper():
        # Look for the next two lines that start with "1" and "2"
        line1 = None
        line2 = None
        for j in range(i + 1, min(i + 5, len(lines))):  # Check next few lines
            if lines[j].strip().startswith("1 "):
                line1 = lines[j].strip()
            elif lines[j].strip().startswith("2 "):
                line2 = lines[j].strip()
                break
        
        if line1 and line2:
            iss_data = {
                'name': lines[i].strip(),
                'line1': line1,
                'line2': line2
            }
            break

if not iss_data:
    print("❌ Could not find ISS in the data!")
    exit()

print(f"🎯 Found: {iss_data['name']}")

# Extract basic orbital elements from TLE data
line2 = iss_data['line2']

if len(line2) >= 69:
    inclination = float(line2[8:16].strip())     # Inclination in degrees
    raan = float(line2[17:25].strip())           # Right Ascension of Ascending Node
    eccentricity = float("0." + line2[26:33])    # Eccentricity
    arg_perigee = float(line2[34:42].strip())    # Argument of perigee
    mean_anomaly = float(line2[43:51].strip())   # Mean anomaly
    mean_motion = float(line2[52:63].strip())    # Mean motion (orbits per day)

print(f"📊 ISS Orbital Data:")
print(f"   Inclination: {inclination:.1f}°")
print(f"   Mean Motion: {mean_motion:.2f} orbits/day")
print(f"   Orbital Period: {24/mean_motion:.1f} hours")

# Calculate orbit radius using semi-major axis (SMA) from mean motion
# Using Kepler's 3rd law: n² = GM/a³, where n = mean motion, a = semi-major axis
earth_radius = 6371  # km
earth_mu = 398600.4418  # Earth's gravitational parameter (km³/s²)
orbital_period_seconds = (24 * 3600) / mean_motion
mean_motion_rad_per_sec = (2 * math.pi) / orbital_period_seconds

# Calculate semi-major axis using Kepler's 3rd law
semi_major_axis = (earth_mu / (mean_motion_rad_per_sec ** 2)) ** (1/3)
orbit_radius = semi_major_axis
altitude = orbit_radius - earth_radius

print(f"   Semi-major axis: {semi_major_axis:.0f} km")
print(f"   Altitude: {altitude:.0f} km")

# Create the plot
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# Draw Earth as a blue circle
earth = plt.Circle((0, 0), earth_radius, color='lightblue', label='Earth')
ax.add_patch(earth)

# Draw continents as visible green patches on Earth
import matplotlib.patches as patches

# North America (top-left of Earth)
north_america = plt.Circle((-earth_radius*0.3, earth_radius*0.3), earth_radius*0.25, 
                          color='green', alpha=0.9, clip_on=True)
ax.add_patch(north_america)

# Europe/Africa (center-right of Earth)  
europe_africa = plt.Circle((earth_radius*0.2, 0), earth_radius*0.3, 
                          color='green', alpha=0.9, clip_on=True)
ax.add_patch(europe_africa)

# Asia (top-right of Earth)
asia = plt.Circle((earth_radius*0.3, earth_radius*0.4), earth_radius*0.2, 
                 color='green', alpha=0.9, clip_on=True)
ax.add_patch(asia)

# Australia (bottom-right of Earth)
australia = plt.Circle((earth_radius*0.4, -earth_radius*0.4), earth_radius*0.15, 
                      color='green', alpha=0.9, clip_on=True)
ax.add_patch(australia)

# Generate orbit path points
num_points = 100
orbit_angles = np.linspace(0, 2 * np.pi, num_points)

# Create orbit coordinates (simplified - circular orbit)
# Rotate by inclination angle
orbit_x = []
orbit_y = []

for angle in orbit_angles:
    # Basic circular orbit
    x = orbit_radius * np.cos(angle)
    y = orbit_radius * np.sin(angle) * np.cos(np.radians(inclination))
    orbit_x.append(x)
    orbit_y.append(y)

# Plot the orbit
ax.plot(orbit_x, orbit_y, 'r-', linewidth=2, label=f'{iss_data["name"]} Orbit')

# Calculate current ISS position (simplified)
current_angle = np.radians(mean_anomaly)
iss_x = orbit_radius * np.cos(current_angle)
iss_y = orbit_radius * np.sin(current_angle) * np.cos(np.radians(inclination))

# Plot current ISS position
ax.plot(iss_x, iss_y, 'ro', markersize=10, label='Current ISS Position')

# Add arrow showing orbital direction
next_angle = current_angle + 0.2
next_x = orbit_radius * np.cos(next_angle)
next_y = orbit_radius * np.sin(next_angle) * np.cos(np.radians(inclination))
ax.arrow(iss_x, iss_y, (next_x - iss_x) * 0.3, (next_y - iss_y) * 0.3, 
         head_width=200, head_length=300, fc='red', ec='red')

# Set up the plot
ax.set_xlim(-orbit_radius * 1.2, orbit_radius * 1.2)
ax.set_ylim(-orbit_radius * 1.2, orbit_radius * 1.2)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend()

# Add labels and title
ax.set_xlabel('Distance (km)')
ax.set_ylabel('Distance (km)')
ax.set_title(f'{iss_data["name"]} Orbit Around Earth\nInclination: {inclination:.1f}°, Period: {24/mean_motion:.1f} hours')

# Add some helpful text
ax.text(0, -orbit_radius * 1.05, 'Earth', ha='center', fontsize=12, weight='bold')
ax.text(iss_x, iss_y + 500, 'ISS Here!', ha='center', fontsize=10, 
        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))

print(f"\n🎨 Creating plot...")
plt.tight_layout()

# Save the plot
plt.savefig('iss_orbit.png', dpi=150, bbox_inches='tight')
print("💾 Saved plot as 'iss_orbit.png'")

# Show the plot
plt.show()

print(f"\n🎉 Success! You've visualized the ISS orbit around Earth!")
print(f"💡 The ISS completes one orbit every {24/mean_motion:.1f} hours")
print(f"   It travels at about {2 * np.pi * orbit_radius / (24/mean_motion) / 3600:.1f} km/s!")