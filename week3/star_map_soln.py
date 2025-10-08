import pandas as pd
import math
import py5

df = 0
border = 0

def load_data():
    global df
    df = pd.read_csv("data/HabHYG15ly.csv", encoding="latin1")
    count = df.shape[1]
    print(f"Num stars: {count}")
    pass

def print_stars():

    for i in range(5):
        print(df['Display Name'][i])

    print()
    for i, row in df.iterrows():
        if i == 5:
            break
        print(row['Display Name'])
        print(row['Xg'])
        print(row['Yg'])
        print(row['Zg'])
        print(row['Hab?'])

    # also!

    print(df.head())
        
    pass

# 8 0, 10, 0, 20
def remap(a, b, c, d, e):
    range1 = c -b
    range2 = e - d
    how_far = a - b
    return d + (how_far / range1) * range2


    return 0

print (py5.remap(10, 0, 100, 200, 400))
print(remap(10, 0, 100, 200, 400))

print (py5.remap(-5, -20, 200, 200, 100))
print(remap(-5, -20, 200, 200, 100))


def draw_grid():
    global border

    for i in range(-5, 6):
        py5.stroke(0, 255, 0)
        x = py5.remap(i, -5, 5, border, py5.width - border)
        y = py5.remap(i, -5, 5, border, py5.height - border)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.fill(255)
        py5.text(i, x, border * 0.5)
        py5.text(i, border * 0.5, y)
        
        py5.line(x, border, x, py5.height - border)
        py5.line(border, y, py5.width - border, y)


def draw_stars():
    global df
    global border

    for i, row in df.iterrows():
        xg = row['Xg']
        x = py5.remap(xg, -5, 5, border, py5.width - border)
        yg = row['Yg']
        y = py5.remap(yg, -5, 5, border, py5.height - border)
        py5.no_fill()
        py5.stroke(0, 255, 255)
        w = row['AbsMag']
        py5.circle(x, y, w)
        py5.stroke(255, 255, 0)
        py5.line(x, y -5, x, y + 5)
        py5.line(x-5, y, x + 5, y)
        py5.text_align(py5.LEFT, py5.CENTER)
        py5.text(row['Display Name'], x + 20, y)

def dist(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))        

def mouse_pressed():
    global clicked1, clicked0, border


    inside = None
    for i, row in df.iterrows():
        xg = row['Xg']
        x = py5.remap(xg, -5, 5, border, py5.width - border)
        yg = row['Yg']
        y = py5.remap(yg, -5, 5, border, py5.height - border)
        
        d = dist(py5.mouse_x, py5.mouse_y, x, y)
        name = row['Display Name']
        if d < (row['AbsMag']):
            inside = row
            break

    if clicked0 is None and clicked1 is None:
        if inside is not None:
            clicked0 = inside
        pass
    elif clicked0 is not None and clicked1 is None:
        if inside is not None:
            clicked1 = inside
        pass
    elif inside is not None:
        clicked0 = inside
        clicked1 = None
    else:
        clicked0 = None
        clicked1 = None
    
clicked0 = None
clicked1 = None

def setup():
    global border

    py5.size(500, 500)
    border = py5.width * 0.1
    load_data()
    print_stars()


def draw():
    global clicked0, clicked1, border
    py5.background(0)
    py5.stroke(255)
    draw_grid()
    draw_stars()

    if clicked0 is not None and clicked1 is None:
        xg = clicked0['Xg']
        yg = clicked0['Yg']
        x = py5.remap(xg, -5, 5, border, py5.width - border)
        y = py5.remap(yg, -5, 5, border, py5.height - border)
        
        py5.line(x, y, py5.mouse_x, py5.mouse_y)
    elif clicked0 is not None and clicked1 is not None:
        p0 = (clicked0['Xg'], clicked0['Yg'], clicked0['Zg'])
        p1 = (clicked1['Xg'], clicked1['Yg'], clicked1['Zg'])
        
        dist = math.dist(p0, p1)

        py5.fill(255)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(f"The distance between {clicked0['Display Name']} and {clicked1['Display Name']} is {dist} parsecs"
                 , py5.width / 2
                 , py5.height - 25)

py5.run_sketch()