# 🌍 Step 2: Plot a Satellite Orbit ✅

Now let's visualize what we downloaded! We'll create a professional satellite tracking visualization that shows the ISS orbit over a real world map using advanced Python libraries.

## 🎯 What We're Going to Create

A professional satellite tracking plot showing:
- 🌍 **Real Earth Map** with continents, oceans, and coastlines
- 🛰️ **ISS orbit trace** as a curved red line around Earth (with proper dateline crossing handling)
- 📍 **Current ISS position** as a red dot with annotation showing real-time location
- 📊 **Orbital information** including inclination, altitude, and period

## 🐍 Create Your Orbit Plotter

**🎯 Step-by-step:**

1. **Copy your satellite data** from step 1:
   ```powershell
   copy ..\step1_get_satellites\satellites.txt .
   ```
   (Or manually copy the `satellites.txt` file to this folder)

2. **Ask Copilot to create the plotting script**:
   Open Copilot Chat (`Ctrl+Alt+I`) and ask:
   ```
   Create a Python script called plot_satellite.py that:
   1. Reads satellites.txt and finds the ISS satellite
   2. Uses the Skyfield library for accurate satellite calculations
   3. Creates a world map using Cartopy with real Earth features
   4. Plots the ISS orbit path with proper dateline crossing handling
   5. Shows the current ISS position as a red dot with annotation
   6. Displays orbital information (inclination, period, altitude)
   7. Handles longitude discontinuities to avoid horizontal line artifacts
   
   Requirements:
   - Use Skyfield for professional satellite tracking accuracy
   - Use Cartopy for real world map projection
   - Handle dateline crossings properly in orbit traces
   - Show current real-time ISS position and altitude
   ```

3. **Install required libraries**:
   The script needs several libraries. Ask Copilot:
   ```
   I need to install the required Python packages for satellite plotting:
   matplotlib, cartopy, skyfield, numpy
   
   Please help me install these packages.
   ```

## 📊 What Your Plot Should Look Like

Your script should create a professional world map plot showing:

**🌍 Real Earth Map Features:**
- **Ocean areas**: Light blue colored regions
- **Land masses**: Green colored continents
- **Coastlines**: Detailed country borders
- **Grid lines**: Latitude/longitude reference lines

**🛰️ ISS Orbital Elements:**
- **Red curved line**: ISS orbit trace for one complete orbit
- **Red dot**: Current real-time ISS position
- **Yellow annotation**: "ISS CURRENT POSITION" with arrow
- **Equator line**: Dashed red reference line

**📊 Information Display:**
- **Title**: Shows inclination, altitude, and orbital period
- **Current position**: Latitude and longitude coordinates
- **Orbital data**: Period in minutes, altitude in km

## 🔍 Understanding the TLE Data and Skyfield Integration

The script uses professional-grade satellite tracking through Skyfield library:

```
ISS (ZARYA)
1 25544U 98067A   23345.12345678  .00001234  00000-0  12345-4 0  9991
2 25544  51.6416  21.1234 0001234 123.4567 234.5678 15.54321098765432
```

**🎯 Key Data Extracted:**
- **Inclination**: ~51.6° (orbit tilt relative to equator)
- **Mean Motion**: ~15.5 orbits per day
- **Orbital Period**: ~92.9 minutes per orbit
- **Altitude**: ~420-425 km above Earth

**🔧 Technical Features:**
- **Skyfield Integration**: Uses professional SGP4 model for accurate calculations
- **Real-time Positioning**: Calculates current ISS position with kilometer precision
- **Dateline Handling**: Prevents horizontal line artifacts when orbit crosses ±180° longitude
- **Cartopy Mapping**: Uses Natural Earth data for realistic world map projection

## ✅ Verify Your Success

Your script should accomplish:
- ✅ Parse ISS TLE data from satellites.txt file
- ✅ Calculate accurate orbital parameters using Skyfield
- ✅ Generate real-time ISS position coordinates
- ✅ Create world map with Cartopy (continents, oceans, borders)
- ✅ Plot complete ISS orbit trace without horizontal line artifacts
- ✅ Display current ISS position with annotation
- ✅ Save high-resolution plot as 'iss_orbit_world_map.png'

**🎉 Success indicators:**
- **Console Output**: Shows ISS orbital data (inclination: 51.6°, period: 92.9 min, altitude: ~424 km)
- **World Map**: Realistic Earth projection with green land and blue oceans
- **Orbit Trace**: Smooth red curved line showing ISS ground track
- **Current Position**: Red dot with yellow annotation showing real-time location
- **Proper Scaling**: No horizontal lines across the map (dateline crossings handled correctly)
- **File Output**: High-quality PNG image saved successfully

## 🎯 What We're Learning

This step teaches advanced satellite visualization concepts:

- 📊 **Professional Data Visualization**: Using matplotlib + Cartopy for publication-quality plots  
- 🌍 **Geographic Projections**: Real-world map projections and coordinate transformations
- 🛰️ **Satellite Tracking**: Professional SGP4 orbital model through Skyfield library
- 📐 **Computational Geometry**: Handling longitude discontinuities and dateline crossings
- ⏰ **Real-time Calculations**: Computing current satellite positions with high accuracy
- 🎨 **Cartographic Design**: Creating informative, visually appealing orbital visualizations

**🔑 Key Technical Insights:**
- **Professional Libraries**: Skyfield provides NASA-quality satellite calculations
- **Coordinate Challenges**: Longitude wrapping requires special handling to avoid visual artifacts
- **Real-time Precision**: Modern satellite tracking achieves kilometer-level accuracy
- **Orbital Predictability**: Satellites follow precise, calculable paths governed by physics

## 💡 Advanced Extensions (Optional)

Once your professional satellite tracker works, you could ask Copilot to help you:

**🚀 Multi-Satellite Tracking:**
- Plot multiple satellites (Starlink constellation, GPS satellites)
- Color-code satellites by type or altitude
- Show satellite coverage areas and ground stations

**⏰ Time-Based Features:**
- Animate ISS movement over time using matplotlib animation
- Predict future ISS passes over specific locations
- Show orbital decay and station-keeping maneuvers

**🌍 Geographic Enhancements:**
- Add major cities and population centers
- Show day/night terminator line
- Display ground track history for multiple orbits

**📊 Data Analysis:**
- Compare orbital elements between different satellites
- Analyze orbital period changes over time
- Calculate satellite visibility windows from your location

---

**Previous:** [👈 Step 1: Get Satellite Data](../step1_get_satellites/README.md)

**Next:** Step 3: Real-time Tracking (coming soon!)
