import pandas as pd
import py5

df = pd.read_csv("data/HabHYG15ly.csv", encoding="latin-1")

dist = df['Distance'][1]
display_name = df['Display Name'][1]

col = df['HabHyg']

print(col)
print(dist)
print(display_name)

print(df.shape)

print(df.shape[0]) # row count
print(df.shape[1]) # column count

def draw_grid():
    border = 50

    for i in range(-5, 6):
        x = py5.remap(i, -5, 5, border, py5.width - border)
        y = py5.remap(i, -5, 5, border, py5.height - border)
        py5.text_align(py5.CENTER, py5.CENTER)
        py5.text(i, x, 25)
        py5.text(i, 25, y)
        
        py5.line(x, border, x, py5.height - border)
        py5.line(border, y, py5.width - border, y)

for i, row in df.iterrows():
    print(i)
    display_name = row['Display Name']
    xg = row['Xg']
    x = py5.remap(xg, -5, 5, 0, py5.width)
    print(display_name)

def draw_stars():
    global df
    global border
    for i, row in df.iterrows():
        xg = row['Xg']
        x = py5.remap(xg, -5, 5, border, py5.width - border)
        yg = row['Yg']
        y = py5.remap(yg, -5, 5, border, py5.height - border)
        py5.no_fill()
        py5.circle(x, y, 10)

s = "I love Pythin"

l = s[2:6]
print(l)
border = 50

py = s[-6:len(s)]
print(py)

rainfall = [300, 400, 800, 400, 200, 100, 50, 25, 100, 200, 300, 400]

print(len(rainfall))

print("Rainfall")
i = 0
for r in rainfall:
    print(r) 

for i in range(len(rainfall)):
    print(rainfall[i])

def remap(a, b, c, d, e):
    range1 = c -b
    range2 = e - d
    how_far = a -b

    return d + (how_far / range1) * range2

def setup():
    py5.size(500, 500)

    for i in range(10):
        print (i)
        print(py5.remap(i, 0, 10, 200, 300))
        print(py5.remap(i, -5, 5, -50, 50))

        print(remap(i, 0, 10, 200, 300))

def draw():
    py5.background(0)
    py5.stroke(255)
    draw_grid()
    draw_stars()
    w = py5.width / len(rainfall)
    for i in range(len(rainfall)):
        x = py5.remap(i, 0, len(rainfall), 0, py5.width)
        # py5.rect(x, py5. height, w, - rainfall[i])

py5.run_sketch()