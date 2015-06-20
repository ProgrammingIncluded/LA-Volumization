import pygame

from SimpleCV import Image, Color, Camera, Display
from pygame import event

from CMDLoader import CMDLoader

app = CMDLoader()
app.inputInfo()
app.displayDataInput()
app.displayResult()


#cam = Camera()
#Display object.
#display = Display((640,480))

#while not display.isDone():
        # Exit code.
#       img = cam.getImage()
#	img.show()
