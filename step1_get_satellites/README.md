
# 🚀 Step 1: Get Satellite Data

Before we can answer our big question, we need a source of data that's trustworthy, always available, and (ideally) free. For satellites, one of the best sources is Celestrak—a public website used by scientists, engineers, and space agencies around the world.

## 👀 See Satellite Data for Yourself

Let's start by looking at real satellite data! 🛰️

**📋 Step-by-step:**
1. Open your web browser and go to <a href="https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle" target="_blank" rel="noopener noreferrer">Celestrak</a>
2. You should see a page full of text. This is called "TLE data"  (Two-Line Element data) and it describes the orbits of satellites.

<details>
<summary><strong>What is TLE Data?</strong> (click to expand)</summary>

When you look at the Celestrak page, you'll see blocks of text like this:

```
ISS (ZARYA)
1 25544U 98067A   23345.12345678  .00001234  00000-0  12345-4 0  9991
2 25544  51.6416  21.1234 0001234 123.4567 234.5678 15.54321098765432
```

- The first line is the satellite's name (like "ISS (ZARYA)").
- The next two lines are the "Two-Line Element" (TLE) data. These numbers describe the satellite's orbit—like its path, speed, and position in space.

**Visual Guide:**

| Line | What it means       |
|------|---------------------|
| 1    | Satellite name      |
| 2    | Orbit info (part 1) |
| 3    | Orbit info (part 2) |

You don't need to understand all the numbers yet—just know that this is the data we'll use to find satellites!

</details>


3. Scroll through the page. Each satellite has a name and two lines of numbers. Can you spot the pattern?
4. Try searching (Ctrl+F) for a satellite name you recognize, like "Starlink". There are thousands!
5. When you're ready, come back here and we'll learn how to download this data with Python!

## 🐍 Your First Python Program: Download Satellite Data

Now let's use GitHub Copilot to help us write Python code that downloads satellite data! 🤖

**🎯 Step-by-step:**

1. Open Copilot Chat by pressing `Ctrl+Alt+I` (or `Ctrl+Cmd+I` on Mac).

2. Ask Copilot to create the file for you: "Create an empty Python file called get_satellites.py in this folder and let's work on it together."

3. In the chat, ask: "Write a simple Python script to download all satellite data from celestrak and save it to a file called satellites.txt"

4. ⚠️ **Important:** If Copilot suggests complex code with classes or functions, ask it to simplify! Try these follow-up prompts:
   - "Make this simpler for a beginner"
   - "Can you write this without functions or classes?"
   - "I want the shortest possible code that just downloads and saves the file"

5. If you need help understanding any part of the code, ask Copilot Chat:
   - "What does this line do?"
   - "Can you explain this code step by step?"

6. 🎉 Run your program and see if it creates a `satellites.txt` file with real satellite data!

<details>
<summary><strong>🔧 Troubleshooting: Missing Modules</strong> (click if you get errors)</summary>

If you get an error like `ModuleNotFoundError: No module named 'requests'`, don't worry! This is normal and a great chance to practice with Copilot.

**Ask Copilot for help:**
1. Press `Ctrl+I` (or `Cmd+I` on Mac) to open Copilot Chat
2. Ask: "I got a ModuleNotFoundError for requests. How do I fix this?"
3. Follow Copilot's suggestions (it will likely tell you to use `pip install requests`)
4. Try running your program again after installing!

**What happened?** The `requests` module isn't included with Python by default—you need to install it first. This is called installing a "package" or "library." Copilot is great at helping with these kinds of setup issues!

</details>

## ✅ Verify Your Success: Check the Downloaded Data

Great! If your Python script ran without errors, you should now have a file called `satellites.txt` with real satellite data. Let's make sure it worked! 🔍

**🎯 Step-by-step verification:**

1. **Find your new file:** Look in the same folder as your `get_satellites.py` file. You should see a new file called `satellites.txt`.

2. **Open the file:** Double-click on `satellites.txt` to open it in VS Code (or any text editor).

3. **Compare with the source:** 
   - Open the <a href="https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle" target="_blank" rel="noopener noreferrer">Celestrak page</a> in your browser
   - Compare the first few satellites in your `satellites.txt` file with what you see on the Celestrak website
   - They should look identical!
   - **Reference examples:** You can also compare with our <a href="https://github.com/traviswillett/hi_ai/blob/main/step1_get_satellites/example_get_satellites.py" target="_blank" rel="noopener noreferrer">example script</a> and <a href="https://github.com/traviswillett/hi_ai/blob/main/step1_get_satellites/example_satellites.txt" target="_blank" rel="noopener noreferrer">example output</a>

4. **What to look for:**
   - Your file should start with satellite names and TLE data, just like the website
   - You should see familiar satellites like "ISS (ZARYA)" or "STARLINK" entries
   - The format should match: name on one line, then two lines of numbers

5. **Check the file size:** Your `satellites.txt` file should be several hundred KB or larger (it contains thousands of satellites!)

**🎉 Success indicators:**
- ✅ File exists and opens without errors
- ✅ Contains satellite names and TLE data
- ✅ Data matches what you see on Celestrak website
- ✅ File is large (lots of satellites!)

**🚨 If something doesn't look right:**
- 💬 Ask Copilot Chat: "My satellites.txt file doesn't look right. Can you help me debug my script?"
- 🌐 Check if your internet connection was working when you ran the script
- 🔄 Try running your Python script again

## 🎯 What Did We Just Accomplish?

🎉 **Congratulations!** You just wrote your first AI-assisted Python program that:

- 🌐 **Connected to the internet** to fetch real-time satellite data
- 📊 **Downloaded thousands of satellite records** from a scientific database
- 💾 **Saved the data to a file** for future use
- 🤖 **Used GitHub Copilot** as your coding assistant

This is the foundation for answering our big question: "How many satellites are overhead right now?" In the next steps, we'll learn how to filter this data for your specific location and visualize it! 🗺️

---

**Next:** [🌍 Step 2: Plot Satellite Orbits](../step2_data_processing/README.md)