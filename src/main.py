import pygame

from SimpleCV import Image, Color, Camera, Display
from pygame import event

from Snap import Snap
from Slice import BlockSlice
from DataPoint import DataPoint

test = Snap(2)
test.addPoint(DataPoint(0, 1, 1))
test.addPoint(DataPoint(1, 1, 1))
slice = BlockSlice(test, test, 90);
print slice.getAreaTwo() * slice.getAreaOne()

#cam = Camera()
#Display object.
#display = Display((640,480))

#while not display.isDone():
        # Exit code.
#       img = cam.getImage()
#	img.show()
