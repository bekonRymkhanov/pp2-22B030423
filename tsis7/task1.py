import pygame
import math
import datetime
def hell(a):
    x,y=0,0
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
    return x,y
pygame.init()

clock=pygame.time.Clock()
height,width=500,500
screen=pygame.display.set_mode((height,width))
pygame.display.set_caption("mickey mouse clock")

image=pygame.image.load("better.png")
reimage=pygame.transform.scale(image,(height+25,width))

secondhands=pygame.image.load("hands.png")
resecondhands=pygame.transform.scale(secondhands,(220,10))

minutehands=pygame.image.load("hands.png")
reminutehands=pygame.transform.scale(minutehands,(220,20))

hourhands=pygame.image.load("hands.png")
rehourhands=pygame.transform.scale(hourhands,(220,30))
runned=True

while runned:
    hours=datetime.datetime.now().hour
    if hours>12:
        hours-=12

    a=-270+datetime.datetime.now().second*-6
    b=-270+datetime.datetime.now().minute*-6
    c=-270+hours*-30

    screen.fill((255,255,255))

    screen.blit(reimage,(0,0))

    rotatedimage=pygame.transform.rotate(resecondhands,a)
    screen.blit(rotatedimage,(height/2-hell(a)[0],width/2-hell(a)[1]-5))

    rotatedsecondhands=pygame.transform.rotate(reminutehands,b)
    screen.blit(rotatedsecondhands,(height/2-hell(b)[0],width/2-hell(b)[1]-10))

    rotatedminutehands=pygame.transform.rotate(rehourhands,c)
    screen.blit(rotatedminutehands,(height/2-hell(c)[0],width/2-hell(c)[1]-15))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()
    clock.tick(20)