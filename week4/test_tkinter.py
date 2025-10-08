import py5
import tkinter as tk

# Shared variables
bg_color = 128
circle_size = 50
circle_x = 300
circle_y = 300

def setup():
    py5.size(600, 600)

def draw():
    py5.background(bg_color)
    py5.fill(255, 100, 100)
    py5.circle(circle_x, circle_y, circle_size)

# Start py5 FIRST in non-blocking mode
py5.run_sketch(block=False)

# Small delay to let py5 initialize
import time
time.sleep(0.3)

# Create tkinter window
root = tk.Tk()
root.title("py5 Controls")
root.geometry("300x350")

# Background slider
tk.Label(root, text="Background Color").pack(pady=5)
def update_bg(val):
    global bg_color
    bg_color = int(val)

bg_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, command=update_bg)
bg_slider.set(128)
bg_slider.pack(fill=tk.X, padx=20)

# Size slider
tk.Label(root, text="Circle Size").pack(pady=5)
def update_size(val):
    global circle_size
    circle_size = int(val)

size_slider = tk.Scale(root, from_=10, to=200, orient=tk.HORIZONTAL, command=update_size)
size_slider.set(50)
size_slider.pack(fill=tk.X, padx=20)

# X position
tk.Label(root, text="X Position").pack(pady=5)
def update_x(val):
    global circle_x
    circle_x = int(val)

x_slider = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL, command=update_x)
x_slider.set(300)
x_slider.pack(fill=tk.X, padx=20)

# Y position
tk.Label(root, text="Y Position").pack(pady=5)
def update_y(val):
    global circle_y
    circle_y = int(val)

y_slider = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL, command=update_y)
y_slider.set(300)
y_slider.pack(fill=tk.X, padx=20)

# Reset button
def reset_all():
    global bg_color, circle_size, circle_x, circle_y
    bg_color = 128
    circle_size = 50
    circle_x = 300
    circle_y = 300
    bg_slider.set(128)
    size_slider.set(50)
    x_slider.set(300)
    y_slider.set(300)

tk.Button(root, text="Reset", command=reset_all, bg="red", fg="white").pack(pady=20)

# Run tkinter
root.mainloop()