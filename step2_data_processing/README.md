# 🔍 Step 2: Data Processing

We downloaded thousands of satellites in Step 1, but looking at a text file with 77,000+ lines isn't very helpful. Let's create visual plots to understand what we actually collected.

This is also a perfect opportunity to learn something important about working with AI: **the way you ask for help completely changes what you get.**

## 🎯 What We Want to Understand

Looking at our `satellites.txt` file, we have questions like:
- How many satellites did we actually download?
- What types of satellites are up there? (Military? Commercial? Scientific?)
- Where are they? Can we see them moving around Earth?
- How can we visualize this data to make sense of it?

## 🧪 Experiment: Two Ways to Ask for Help

### Round 1: The Simple Request

Let's start by asking AI the way most people naturally would:

1. **Copy your satellite data** from step 1:
   ```powershell
   copy ..\step1_get_satellites\satellites.txt .
   ```

2. **Ask Copilot the obvious question**:
   Open Copilot Chat (`Ctrl+I`) and ask:
   
   > Plot the satellites in satellites.txt

3. **Run whatever it creates**:
   - Accept whatever filename Copilot suggests
   - Install any packages it recommends
   - Run the script and see what happens

4. **Observe the results**:
   - What type of visualization did it create?
   - What did it focus on showing you?
   - What questions do you still have?

### Round 2: The Detailed Request

Now let's try being much more specific about what we want:

5. **Ask for something specific**:
   This time, be very clear about what you want to see:
   
   > I want to visualize the International Space Station (ISS) from my satellite data. 
   > Create a Python script called iss_tracker.py that:
   > 1. Finds the ISS in my satellites.txt file
   > 2. Shows where it is right now over a real world map
   > 3. Draws its orbit path around Earth
   > 4. Uses professional satellite tracking libraries for accuracy
   > 5. Shows me orbital details like altitude and how long one orbit takes
   > 
   > Please use Skyfield library for satellite calculations and Cartopy for the world map.
   > I want to see continents, oceans, and the ISS position marked clearly.

6. **Install the professional tools**:
   When Copilot asks about packages:
   
   > Please help me install matplotlib, cartopy, skyfield, and numpy for satellite visualization.

7. **Compare the results**:
   - Run both scripts and compare what they show you
   - Which one helps you understand your satellite data better?
   - Which one looks more professional?

## 🔍 What You'll Discover

**Simple request results:**
- Basic counting and categorization of satellites
- Simple bar chart showing satellite distribution
- Quick overview of your dataset

**Detailed request results:**
- Real-time ISS tracking on a world map
- Professional visualization with orbital calculations
- Shows how satellites actually move in space

**The lesson:** Same data, same AI assistant, completely different results based on how you asked.

## 💡 Why This Matters

**AI needs context to help you effectively:**
- Simple requests get basic solutions
- Specific requests with technical details get professional-quality results
- You don't need to be an expert to ask for sophisticated tools

**Tips for better AI conversations:**
- Start simple to see what happens, then be more specific
- Mention professional libraries even if you don't know them well
- Describe your end goal clearly ("track the ISS" vs. "plot data")

## ✅ Verify Your Understanding

After completing both experiments, you should have:
- Two different scripts showing different approaches
- Understanding of how prompt specificity affects results
- Knowledge about your satellite dataset
- Experience with both basic and professional Python visualization techniques

## 🚀 What's Next

Now that you understand your satellite data and how to work effectively with AI, you can:
- Try tracking other satellites beyond the ISS
- Experiment with different visualization approaches
- Ask for more sophisticated features like animation or interactivity

---

**Previous:** [👈 Step 1: Get Satellite Data](../step1_get_satellites/README.md)

**Next:** Step 3: Real-time Tracking (coming soon!)