"""
Turtle Spiral Pattern Generator 🌀🌈
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python
Description: This script uses the turtle graphics library to create a colorful spiral pattern
using HSV color gradients. It demonstrates drawing loops, dynamic color generation,
and turtle movement to produce mesmerizing visual art. ✨
"""

# Import everything from turtle and only 'hsv_to_rgb' from colorsys
from turtle import *
from colorsys import hsv_to_rgb

# Set background color to black for better contrast with colors
bgcolor("black")

# Set the drawing pen width
width(2)

# 'h' will be used to gradually change hue in HSV color space
h = 0.0

# Loop 250 times to draw the spiral pattern
for i in range(250):

    # Set turtle drawing speed (1 slowest – 10 fast – 0 instant)
    speed(18)

    # Convert current hue to RGB color
    # hsv_to_rgb returns values between 0 and 1, which turtle accepts
    color(hsv_to_rgb(h, 1, 1))

    # Move forward — the distance increases with each iteration
    forward(i * 2)

    # Turn the turtle at a fixed angle to start forming the spiral
    right(121)

    # Slightly increase hue so next color is different
    h += 0.005

# End the drawing properly and keep the window open
done()
