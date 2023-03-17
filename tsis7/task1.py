import pygame
import math
import datetime
pygame.init()

clock=pygame.time.Clock()

screen=pygame.display.set_mode((700,500))
pygame.display.set_caption("mickey mouse clock")

image=pygame.image.load("mickeyall.jpg")
resizedimage=pygame.transform.scale(image,(700,500))

image1=pygame.image.load("hands.png")
resizedimage1=pygame.transform.scale(image1,(220,15))

image2=pygame.image.load("hands.png")
resizedimage2=pygame.transform.scale(image2,(220,30))
runned=True
x,y,x2,y2=0,0,0,0
while runned:
    a=-270+datetime.datetime.now().second*-6
    b=-270+datetime.datetime.now().minute*-6
    if abs(a)>360:
        a+=360
    if abs(a)<=90:
        pass
    elif abs(a)>90 and abs(a)<=180:
        deg=(a-90)/57.2958
        x+=math.sin(deg)*220
    elif abs(a)<=270 and abs(a)>=180:
        deg=(a-180)/57.2958
        y-=math.sin(deg)*220
        x+=math.cos(deg)*220
    elif abs(a)<=360 and abs(a)>=270:
        deg=(a-270)/57.2958
        y-=math.cos(deg)*220


    if abs(b)>360:
        b+=360
    if abs(b)<=90:
        pass
    elif abs(b)>90 and abs(b)<=180:
        deg=(b-90)/57.2958
        x2+=math.sin(deg)*220
    elif abs(b)<=270 and abs(b)>=180:
        deg=(b-180)/57.2958
        y2-=math.sin(deg)*220
        x2+=math.cos(deg)*220
    elif abs(b)<=360 and abs(b)>=270:
        deg=(b-270)/57.2958
        y2-=math.cos(deg)*220

    screen.fill((255,255,255))
    screen.blit(resizedimage,(0,0))
    rotatedimage=pygame.transform.rotate(resizedimage1,a)
    screen.blit(rotatedimage,(330-x,235-y))
    rotatedimage1=pygame.transform.rotate(resizedimage2,b)
    screen.blit(rotatedimage1,(330-x2,235-y2))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()
    x,y,y2,x2=0,0,0,0
    clock.tick(20)