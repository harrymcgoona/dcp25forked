# TU850 Data Centric Programming 2025 - SEMESTER 1

```
Welcome to the Metaverse
```

![](holo.jpg)

## Assessment
- 15% Weekly submissions
- 15% Lab Test
- 20% Assignment
- 50% Exam

# Resources
- [CSResources git repo](https://github.com/skooter500/csresources/blob/main/git_ref.pdf). Here you will find links to the previous courses and all my quick references
- [Git for poets](https://www.youtube.com/watch?v=BCQHnlnPusY)
- [Python a Crash Course](https://khwarizmi.org/wp-content/uploads/2021/04/Eric_Matthes_Python_Crash_Course_A_Hands.pdf)
- https://codingbat.com/python
* [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw)
* [The Nature of Code](http://natureofcode.com/)
* [Games Fleadh](http://www.gamesfleadh.ie/)
* [Py5](https://py5coding.org/)


What you will need to install:

- Python
- Java
- VSCode
- Git
- py5
- Pandas
- Maybe more!

## Week 4 - Explore the Tunepal dataset with Pandas

- [Slides](pandas.pdf)

### Lab 

# Irish Music Albums Lab
## Exploring Album and Track Data with Pandas

**Duration:** 2 hours  
**Dataset:** Irish traditional music albums and tracks from thesession.org

---

## Setup

Create a new Python file called `albums_lab.py` and load the two CSV files:
- `album.csv` - Contains album information
- `albumtracktune.csv` - Contains tracks and tunes on each album

**Hint:** Look at the class example for how to load CSV files with pandas.

---

## Part 1: Explore the Albums (20 minutes)

### Task 1.1: Load and Inspect Albums
Load `album.csv` and answer these questions:
- How many albums are in the dataset?
- What are the column names?
- Which artists appear in the first 5 albums?
- Which artists appear in the last 5 albums?

**Hint:** Use `head()`, `tail()`, `shape`, and `info()`

### Task 1.2: Data Types
- What data type is each column?
- Are there any missing values?

**Hint:** Use `info()` and `describe()`

### Task 1.3: Unique Values
Find out:
- How many unique artists are in the dataset?
- Who are the artists?

**Hint:** Look up how to get unique values from a pandas column

---

## Part 2: Explore the Tracks (20 minutes)

### Task 2.1: Load and Inspect Tracks
Load `albumtracktune.csv` and answer:
- How many tracks are in the dataset?
- What columns does this dataset have?
- What is the relationship between this file and the albums file?

**Hint:** Notice the `album_id` column - what does it refer to?

### Task 2.2: Track Numbers
- What's the highest track number on any album?
- How many tunes can a single track contain?

**Hint:** Look at the `track_num` and `tune_num` columns

### Task 2.3: Common Tune Titles
Which tune titles appear most frequently across all albums?

**Hint:** Use `value_counts()` like in the class example

---

## Part 3: Filtering and Counting (25 minutes)

### Task 3.1: Albums by Artist
Filter the albums to show only:
1. Albums by "Altan"
2. Albums by "Martin Hayes"
3. Albums by "The Bothy Band"

How many albums does each artist have in the dataset?

**Hint:** Use boolean indexing like `df[df['column'] == 'value']`

### Task 3.2: Tracks on Specific Albums
1. Find all tracks on album_id 1 (Martin Hayes - The Lonesome Touch)
2. How many tracks are on this album?
3. How many total tunes are on this album?

**Hint:** Filter the tracks dataframe by `album_id`

### Task 3.3: Multi-Tune Tracks
Find all tracks that have more than one tune (tune_num > 1)

How many such tracks are there?

**Hint:** Boolean filtering on the `tune_num` column

---

## Part 4: Grouping and Aggregating (25 minutes)

### Task 4.1: Tracks per Album
Group the tracks by `album_id` and count how many tracks each album has.

Which album has the most tracks?

**Hint:** Use `groupby()` and `count()` or `size()`

### Task 4.2: Tunes per Album
For each album, calculate the total number of tunes (not just tracks - remember some tracks have multiple tunes!)

**Hint:** You might need to count all rows for each album_id

### Task 4.3: Average Tunes per Track
Calculate the average number of tunes per track for each album.

Which albums tend to have more tunes per track?

**Hint:** Use `groupby()` with `mean()` on the `tune_num` column

---

## Part 5: Sorting (15 minutes)

### Task 5.1: Sort Albums
Sort the albums:
1. Alphabetically by title
2. Alphabetically by artist
3. By ID in descending order

**Hint:** Use `sort_values()` with the `ascending` parameter

### Task 5.2: Sort Tracks
Sort the tracks dataframe:
1. By album_id, then by track_num
2. By title alphabetically

**Hint:** You can pass a list of column names to `sort_values()`

---

## Part 6: Merging the Datasets (30 minutes)

Now it's time to combine the two datasets!

### Task 6.1: Simple Merge
Merge the albums and tracks dataframes together so you can see the artist and album title alongside each track.

**Hint:** Look up `pd.merge()` - you'll need to specify which columns to join on. The common column between the two dataframes is the album ID (but it has different names in each dataframe!)

### Task 6.2: Explore the Merged Data
After merging, answer:
- How many rows does the merged dataframe have?
- What new information can you see now that the data is merged?
- Print the first 10 rows

### Task 6.3: Questions with Merged Data
Now that you have both album info and track info together, answer:

1. How many tracks does Martin Hayes have across all his albums?
2. What tunes appear on Altan albums?
3. Which artist has the most individual tune entries in the dataset?

**Hint:** After merging, you can filter by artist name and count

---

## Part 7: Advanced Exploration (25 minutes)

### Task 7.1: Most Prolific Artists
Create a summary showing:
- Each artist
- Number of albums they have
- Total number of tracks across all their albums
- Total number of tunes across all their albums

**Hint:** You'll need to use the merged dataframe and `groupby()` with aggregation

### Task 7.2: Find Repeated Tunes
Some tune titles appear on multiple albums. Find:
1. Which tune title appears most frequently across different albums?
2. Which artists have recorded this tune?

**Hint:** Use `value_counts()` on tune titles, then filter to find those albums

### Task 7.3: Album Completeness
For each album, show:
- Album title
- Artist
- Number of tracks
- Whether all track numbers are sequential (no gaps)

**Hint:** Think about what "sequential" means - track 1, 2, 3, 4... with no missing numbers

---

## Bonus Challenges (If Time Permits)

### Bonus 1: Custom Print Function
Write a function that prints album information nicely formatted:
```
Album: [title]
Artist: [artist]
Tracks: [number]
Tunes: [number]
```

### Bonus 2: Track Listings
Create a function that takes an album_id and prints a complete track listing:
```
Album: The Lonesome Touch by Martin Hayes

Track 1:
  1. Paddy Fahy's
Track 2:
  1. The Kerfunten
Track 3:
  1. Paul Ha'penny
  2. The Garden Of Butterflies
  3. The Broken Pledge
  ...
```

### Bonus 3: Artist Comparison
Compare two artists of your choice:
- How many albums does each have?
- Total tracks?
- Total tunes?
- Do they share any tune titles?

**Hint:** Filter merged data for each artist, then compare

---

## Tips for Success

- **Refer to the class example** - most tasks are variations of what we did with the tune dataset
- **Use print statements** - regularly print your dataframes to see what you're working with
- **Take small steps** - test each piece of code before moving on
- **Check your assumptions** - use `shape`, `head()`, and `info()` frequently
- **Ask for help** - if you're stuck, check with classmates or the instructor

---

## Common Pandas Operations You'll Need

Here's a quick reference (without giving away the answers!):

```python
# Loading
df = pd.read_csv("filename.csv")

# Exploring
df.head()
df.tail()
df.shape
df.info()
df.describe()

# Accessing columns
df['column_name']
df[['col1', 'col2']]

# Filtering
df[df['column'] == value]
df[df['column'] > value]
df[(condition1) & (condition2)]

# Counting
df['column'].value_counts()
df['column'].nunique()

# Grouping
df.groupby('column').count()
df.groupby('column').sum()
df.groupby('column').mean()

# Sorting
df.sort_values('column')
df.sort_values('column', ascending=False)
df.sort_values(['col1', 'col2'])

# Merging
pd.merge(df1, df2, left_on='col1', right_on='col2')
```

---

## Reflection Questions

At the end of the lab, consider:

1. What did you learn about Irish traditional music from this data?
2. What patterns did you notice in how albums are structured?
3. What was the most challenging part of working with these datasets?
4. How did merging the datasets help answer questions you couldn't answer before?
5. What other questions would you like to explore with this data?

---

## Extension Ideas

If you finish early or want to explore further:

- Find albums that share the most tune titles
- Calculate average album length (in tracks) by artist
- Identify "set tunes" - tunes that always appear together on tracks
- Create visualizations of the data
- Export your findings to a new CSV file

---

## What to Submit

Save your Python file with:
- All your code for the tasks
- Comments explaining what each section does
- At least one interesting finding you discovered

**Good luck and have fun exploring the data!** 🎵

## Week 3 - Pandas

### Lab - StarMap Lab - Pandas with py5

[![Video](http://img.youtube.com/vi/J2kHSSFA4NU/0.jpg)](http://www.youtube.com/watch?v=J2kHSSFA4NU)


## Overview

Create an interactive 3D star map visualization using py5 and pandas. You'll load real star data, plot it on a grid, and create interactive features to explore nearby stars.

---

## Task 1: Load the Data

Use pandas to load the `HabHYG15ly.csv` file. This file contains data on stars within 15 light years of the sun.

### Columns of Interest

| Column | Name | Description |
|--------|------|-------------|
| Hab? | Habitability flag | 1 = high probability of habitable planet |
| Display Name | Star name | The name of the star |
| Distance | Distance | Distance from the sun in parsecs |
| Xg, Yg, Zg | Coordinates | XYZ galactic cartesian coordinates in parsecs |
| AbsMag | Magnitude | Star's absolute magnitude (brightness/size) |

### Your Tasks
1. Write a `load_data()` function that loads the CSV with correct encoding
2. Call it from `setup()` and store the DataFrame globally
3. Print the number of stars loaded


## Task 2: Explore the Data

Write a `print_stars()` function that prints useful information about the stars:
- Total number of stars
- First 5 stars with their names, distances, and coordinates
- Any other interesting statistics you find

## Task 3: Draw the Grid

Create a coordinate grid for your star map:

**Requirements:**
- 50 pixel border around the edge
- Grid from -5 to 5 parsecs on both X and Y axes
- Purple gridlines every 1 parsec
- Label each gridline with its parsec value

**Coordinate Conversion:**

```python
py5.remap(parsecs, -5, 5, border, py5.width - border)
```

## Task 4: Plot the Stars

For each star, draw:

1. **Yellow cross** at the star's position (Xg, Yg)
   - About 10 pixels in size
   
2. **Red circle** with diameter based on AbsMag
   - Use `no_fill()` for hollow circles
   - Scale magnitude appropriately (experiment with sizing)

3. **Star name** beside the star
   - Left aligned, vertically centered


## Task 5: Interactive Features

Add mouse interaction to explore star distances.

**Behavior:**
1. **First click:** Select a star, draw yellow line from star to mouse cursor
2. **Second click:** Select another star, draw line between them, display distance

**Display format:**
```
Distance from [STAR1] to [STAR2] is [XX.XX] parsecs
```

**Hints:**
- Use global variables to track selected stars
- Use 3D distance formula: √(dx² + dy² + dz²)
- Check if mouse is within a star's circle radius


---

## Complete Code Template

```python
# Star Map Visualization
# Name: [Your Name]

import py5
import pandas as pd
import math

# Global variables
stars_df = None
selected_star_1 = None
selected_star_2 = None

def load_data():
    """Load star data from CSV"""
    # Your code here
    pass

def print_stars():
    """Print star information"""
    # Your code here
    pass

def parsecs_to_pixels_x(parsecs):
    """Convert parsec X to pixel X"""
    return py5.remap(parsecs, -5, 5, 50, 750)

def parsecs_to_pixels_y(parsecs):
    """Convert parsec Y to pixel Y"""
    return py5.remap(parsecs, -5, 5, 50, 750)

def draw_grid():
    """Draw coordinate grid"""
    # Your code here
    pass

def draw_stars():
    """Draw all stars"""
    # Your code here
    pass

def find_clicked_star(mouse_x, mouse_y):
    """Find which star was clicked"""
    # Your code here
    pass

def calculate_distance(star1, star2):
    """Calculate 3D distance between stars"""
    # Your code here
    pass

def setup():
    py5.size(800, 800)
    global stars_df
    stars_df = load_data()
    print_stars()

def draw():
    py5.background(0)
    draw_grid()
    draw_stars()
    # Add interactive line drawing here

def mouse_pressed():
    """Handle mouse clicks"""
    # Your code here
    pass

py5.run_sketch()
```

---

## Extension Ideas

Once you complete the basic tasks, try:

1. **Color by habitability:** Make habitable stars (Hab? = 1) a different color
2. **Size by distance:** Scale star circles based on distance from Sol
3. **Filter view:** Add keyboard controls to show only certain star types
4. **3D visualization:** Use py5's 3D mode to plot Zg as well
5. **Star info panel:** Display detailed info when hovering over a star
6. **Constellation lines:** Connect related stars

---

## Tips

- Test each task individually before moving to the next
- Use print statements to debug coordinate conversions
- The sun (Sol) should appear at the center (0,0)
- Experiment with scaling factors to make visualization clear
- Use `py5.dist()` for distance calculations in pixel space
- Use the math formula for parsec space distances


## Week 2 - Python Fundamentals

### Lab

Variables exercises:

[![YouTube](http://img.youtube.com/vi/kPOFqXsLLeo/0.jpg)](https://www.youtube.com/watch?v=kPOFqXsLLeo)

If statement Exercises:

[![YouTube](http://img.youtube.com/vi/18kMOeygmHA/0.jpg)](https://www.youtube.com/watch?v=18kMOeygmHA)

- [Learn how to use bash and git](https://github.com/skooter500/csresources/blob/main/gitlab.md)

- [Submit your git repos](https://forms.office.com/Pages/ResponsePage.aspx?id=yxdjdkjpX06M7Nq8ji_V2ou3qmFXqEdGlmiD1Myl3gNUQjhSVU9PUExTV05UNlFNV0JHSjVQMjZFUy4u)

## Week 1 - Introduction to the Course
- Check out [these Sci-Fi user interfaces made by OOP students](https://www.youtube.com/playlist?list=PL1n0B6z4e_E5RZYrubD2pcxq0qzGy-3vr)
- Check out [these music visualisers made in Processing by previous programming students](https://www.youtube.com/watch?v=NGQbYEESZEg&list=PL1n0B6z4e_E7I2bIWWpH8NAa6kPx95sw5)
- If you are curious, check out [some of my creature videos](https://www.youtube.com/watch?v=cW8s5i9dmqA&list=PL1n0B6z4e_E6jErrS0ScSCaVrN7KV729x)

- [Python Notes](week1/python_complete_presentation.pdf)
- [Python Quick Reference (Printable)](week1/python_quick_ref.html)

Write a sketch to draw the following shape:

![Sketch](images/p1.2.png)
