import py5

x = 0.0
y = 0.0
w = 50
dx = 1
dy = 0

def setup():
    global y
    py5.size(500, 500)
    y = py5.height / 2

def draw():
    global x, y, w, dx, dy
    py5.background(0, 255, 0)
    py5.circle(x, y, w)
    x += dx
    y += dy

    for i in range(200, 400, 20):
        py5.line(i, 50, i, 200)
        py5.line(200, i, 250, i)

    # rect(tlx, lty, w, h)
    # fill
    # stroke
    # no_stroke()


py5.run_sketch()


