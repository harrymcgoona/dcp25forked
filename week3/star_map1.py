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

for i, row in df.iterrows():
    print(i)
    display_name = row['Display Name']
    print(display_name)

s = "I love Pythin"

l = s[2:6]
print(l)

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

def setup():
    py5.size(500, 500)

def draw():
    py5.background(0)
    w = py5.width / len(rainfall)
    for i in range(len(rainfall)):
        x = py5.remap(i, 0, len(rainfall), 0, py5.width)
        py5.rect(x, py5. height, w, - rainfall[i])

py5.run_sketch()