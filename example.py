import pygame
pygame.init()
runned=True
Height,Width=800,500
x,y=50,50
dx,dy=0,0
Delta=30
clock=pygame.time.Clock()
screen=pygame.display.set_mode((Height,Width))
pygame.display.set_caption("Katarinai,nemurinai,Toroimenoai,anatano")
while runned:
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(x,y,50,50),0,20)
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        dx=0
        dy=-Delta
    else:
        dx=0
        dy=0
    if pressed[pygame.K_DOWN]:
        dx=0
        dy=Delta
    else:
        dx=0
        dy=0
    if pressed[pygame.K_LEFT]:
        dx=-Delta
        dy=0
    else:
        dx=0
        dy=0
    if pressed[pygame.K_RIGHT]:
        dx=Delta
        dy=0
    else:
        dx=0
        dy=0
    x=x+dx
    y=y+dy
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()
    clock.tick(30)
