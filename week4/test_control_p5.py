import py5

from controlP5 import ControlP5

# Global variable to store the controlP5 instance
cp5 = None
slider_value = 100

def setup():
    global cp5
    py5.size(400, 400)
    
    # Initialize ControlP5 - link it to the current sketch
    cp5 = ControlP5(py5.get_current_sketch())
    
    # Add a slider
    slider = cp5.addSlider("sliderValue") \
       .setPosition(50, 50) \
       .setSize(200, 20) \
       .setRange(0, 255) \
       .setValue(128) \
    
    slider.onChange(lambda event: sliderValue(event.getController().getValue()))
    
    # Add a button
    button = cp5.addButton("myButton") \
       .setPosition(50, 100) \
       .setSize(100, 30) \
    
    button.onClick(lambda event: myButton())
    
    # Add a toggle
    cp5.addToggle("toggle") \
       .setPosition(50, 150) \
       .setSize(50, 20)

def draw():
    py5.background(slider_value)
    
    py5.fill(255)
    py5.text(f"Slider: {slider_value}", 50, 250)

# Event handlers for controlP5
def sliderValue(value):
    global slider_value
    slider_value = value
    print(f"Slider changed to: {value}")

def myButton():
    print("Button pressed!")

def toggle(value):
    print(f"Toggle: {value}")

py5.run_sketch()