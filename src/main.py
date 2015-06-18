import pygame

from SimpleCV import Image, Color, Camera, Display
from pygame import event

cam = Camera()
# Display object.
display = Display((640,480))

while not display.isDone():
        # Exit code.
        if(display.mouseLeft):
                display.done = True

        events = pygame.event.get()
        for event in events:
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESC:
                                display.done = True

        img = cam.getImage()
	img.show()
