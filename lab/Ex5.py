import time
import random

from sense_hat import SenseHat
sense = SenseHat()


# set colors

y = (255, 255, 0)
b = (0, 0, 255)
g = (0, 100, 0)
r = (255, 0, 0)
w = (255, 255, 255)
colorChoice = [y, b, g, r]

# set pattern

image_pixels = [b, b, b, b, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, y, y, y, b, b, b,
                b, y, b, y, b, y, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, b, b, b, b, b,]


# function to change color

def PixelsChangeColor(colorArrow, colorBg):
    image_pixels_new = []

    for i in image_pixels:
        if i == b:
            i = colorBg
        else:
            i = colorArrow
        image_pixels_new.append(i)
    
    return image_pixels_new


# Function to rotate random direction

def GetRandomDirection():
    direction = random.randint(1,4)

    if direction == 1:
        sense.set_rotation(0)
    elif direction == 2:
        sense.set_rotation(90)
    elif direction == 3:
        sense.set_rotation(180)
    else:
        sense.set_rotation(270)
        

# Function to get random colors for arrow and bg

def GetRandomColors():
    
    color1 = random.choice(colorChoice)
    color2 = random.choice(colorChoice)
    while color2 == color1:
        color2 = random.choice(colorChoice)
    
    return color1, color2


def NewGreenArrow():
    
    time.sleep(1)
    GetRandomDirection()
    sense.set_pixels(PixelsChangeColor(g, w))


NewGreenArrow()



# 1 second generate 1 random arrow
'''
# generate new random arrow

def NewRandomArrow():
    
    time.sleep(1)
    GetRandomDirection()
    color3, color4 = GetRandomColors()
    sense.set_pixels(PixelsChangeColor(color3,color4))


# keep getting new random arrow

while True:
    NewRandomArrow()
'''



# first attempt
'''
# display pattern
sense.set_pixels(image_pixels)

# pause 1 second, change random direction, change color to yellow and green
time.sleep(1)
GetRandomDirection()
sense.set_pixels(PixelsChangeColor(y,g))
'''