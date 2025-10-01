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
- -5 parsecs = 50 pixels (left/bottom edge)
- 5 parsecs = 750 pixels (right/top edge)

```python
py5.remap(parsecs, -5, 5, 50, 750)
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