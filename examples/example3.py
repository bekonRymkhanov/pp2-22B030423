import sys
import pygame
import math


class point:
    def __init__(self, xP, yP):
        self.x = xP
        self.y = yP



def drawCircumscribedTriangle(center, radius, window):
    xoffset = math.cos(math.pi/6) * radius
    yoffset = math.sin(math.pi/6) * radius

    pygame.draw.line(window, (255, 255, 255),
                     (center.x, center.y - radius), (center.x + xoffset, center.y + yoffset))
    pygame.draw.line(window, (255, 255, 255),
                     (center.x + xoffset, center.y + yoffset), (center.x - xoffset, center.y + yoffset))
    pygame.draw.line(window, (255, 255, 255),
                     (center.x - xoffset, center.y + yoffset), (center.x, center.y - radius))

pygame.init()

#create the screen
screenWidth = 640
screenHeight = 480
rad = 20
centerPoint = point(screenWidth/2, screenHeight/2)

window = pygame.display.set_mode((640, 480))
drawCircumscribedTriangle(centerPoint, rad, window)

#draw it to the screen
pygame.display.flip()

#input handling (somewhat boilerplate code):
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)