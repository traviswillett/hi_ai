# 🌍 Step 2: Plot a Satellite Orbit

Now let's visualize what we downloaded! We'll take one satellite from our data and plot its orbit around Earth using Python's matplotlib library.

## 🎯 What We're Going to Create

A beautiful plot showing:
- 🌍 **Earth** as a blue circle
- 🛰️ **One satellite's orbit** as a curved line around Earth
- 📍 **Satellite position** at a specific moment in time

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
   Create a simple Python script called plot_satellite.py that:
   1. Reads satellites.txt and finds the ISS satellite
   2. Uses the TLE data to calculate the ISS orbit
   3. Plots Earth as a blue circle
   4. Plots the ISS orbit path around Earth
   5. Shows the current ISS position as a red dot
   6. Uses matplotlib for plotting
   
   Keep it simple - no complex orbital mechanics, just a basic visualization!
   ```

3. **Install matplotlib if needed**:
   If you get a "ModuleNotFoundError", ask Copilot:
   "I need to install matplotlib. How do I do this?"

## 📊 What Your Plot Should Look Like

Your script should create a plot showing:

```
        🛰️ ISS
           •
          /|\
         / | \
        /  |  \    ← ISS orbit path
       /   🌍   \   ← Earth (blue circle)
      \         /
       \       /
        \     /
         \   /
          \ /
           •
```

**Key elements:**
- **Blue circle**: Represents Earth
- **Curved line**: The satellite's orbital path
- **Red dot**: Current satellite position
- **Labels**: Satellite name and basic info

## 🔍 Understanding the TLE Data

We'll focus on these key numbers from the TLE format:

```
ISS (ZARYA)
1 25544U 98067A   23345.12345678  .00001234  00000-0  12345-4 0  9991
2 25544  51.6416  21.1234 0001234 123.4567 234.5678 15.54321098765432
                   ^^^^^^         ^^^^^^^^ ^^^^^^^^
                Inclination    Right Ascension  Mean Anomaly
                (orbit tilt)   (orbit rotation)  (position)
```

**For plotting, we need:**
- **Inclination**: How tilted the orbit is (51.6° for ISS)
- **Right Ascension**: Which direction the orbit points
- **Mean Anomaly**: Where the satellite is in its orbit right now

## ✅ Verify Your Success

Your script should:
- ✅ Find the ISS in the satellite data
- ✅ Create a plot with Earth and orbit
- ✅ Show the satellite's current position
- ✅ Display clearly labeled axes and title
- ✅ Save the plot as an image file

**🎉 Success indicators:**
- Plot opens in a new window
- Earth appears as a blue circle in the center
- Satellite orbit is a tilted ellipse around Earth
- ISS position is marked clearly
- Plot has proper title and labels

## 🎯 What We're Learning

This step teaches:
- 📊 **Data visualization**: Using matplotlib to create plots
- 🌍 **Coordinate systems**: Converting orbital elements to X,Y positions
- 🛰️ **Orbital mechanics basics**: How satellites move around Earth
- 📐 **Geometry**: Working with circles, ellipses, and angles
- 🎨 **Plotting techniques**: Colors, labels, and formatting

**The big insight**: Satellite orbits are predictable! Once we know the orbital elements, we can calculate exactly where a satellite will be at any given time.

## 💡 Fun Extensions (Optional)

Once your basic plot works, you could ask Copilot to help you:
- Plot multiple satellites on the same Earth
- Animate the satellite moving along its orbit
- Show different orbit types (circular vs elliptical)
- Add country borders or your location on Earth

---

**Previous:** [👈 Step 1: Get Satellite Data](../step1_get_satellites/README.md)

**Next:** Step 3: Real-time Tracking (coming soon!)
