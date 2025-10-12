
# Step 1: Get Satellite Data


Before we can answer our big question, we need a source of data that's trustworthy, always available, and (ideally) free. For satellites, one of the best sources is Celestrak—a public website used by scientists, engineers, and space agencies around the world.

---

## See Satellite Data for Yourself

Let's start by looking at real satellite data!

**Step-by-step:**
1. Open your web browser and go to [Celestrak](https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle)
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

---

## Your First Python Program: Download Satellite Data

Now let's use GitHub Copilot to help us write Python code that downloads satellite data!

**Step-by-step:**

1. Create a new file called `get_satellites.py` in this folder.

2. In the new file, type this comment and press `Enter`:
   ```python
   # Download satellite data from Celestrak using Python
   ```

3. Copilot should suggest some code. If it doesn't, try typing:
   ```python
   import requests
   ```

4. Keep typing comments about what you want to do, and let Copilot help you complete the code:
   ```python
   # Get the URL for active satellites
   # Download the data
   # Save it to a file called satellites.txt
   ```

5. Ask Copilot for help if you get stuck! Try pressing `Ctrl+I` (or `Cmd+I` on Mac) and ask questions like:
   - "How do I download a file from a URL in Python?"
   - "How do I save text to a file?"

6. Run your program and see if it creates a `satellites.txt` file with real satellite data!

---

## Troubleshooting: Missing Modules

If you get an error like `ModuleNotFoundError: No module named 'requests'`, don't worry! This is normal and a great chance to practice with Copilot.

**Ask Copilot for help:**
1. Press `Ctrl+I` (or `Cmd+I` on Mac) to open Copilot Chat
2. Ask: "I got a ModuleNotFoundError for requests. How do I fix this?"
3. Follow Copilot's suggestions (it will likely tell you to use `pip install requests`)
4. Try running your program again after installing!

**What happened?** The `requests` module isn't included with Python by default—you need to install it first. This is called installing a "package" or "library." Copilot is great at helping with these kinds of setup issues!