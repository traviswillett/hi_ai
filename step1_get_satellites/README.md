
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