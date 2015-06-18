import pygame

from SimpleCV import Image, Color, Camera, Display
from pygame import event

from Slice import Slice
from DataPoint import DataPoint

test = Slice(2)
test.addPoint(DataPoint())
test.addPoint(DataPoint(1,1,1))
print test

cam = Camera()
# Display object.
display = Display((640,480))

while not display.isDone():
        # Exit code.
        img = cam.getImage()
	img.show()
