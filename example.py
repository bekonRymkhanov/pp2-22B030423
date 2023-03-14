import pygame
pygame.init()
runned=True
Height,Width=800,500
x,y=50,50
Delta=30
clock=pygame.time.Clock()
screen=pygame.display.set_mode((Height,Width))
pygame.display.set_caption("Katarinai,nemurinai,Toroimenoai,anatano")
while runned:
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),pygame.Rect(x,y,50,50),0,20)
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y-=Delta
    if pressed[pygame.K_DOWN]:
        y+=Delta
    if pressed[pygame.K_LEFT]:
        x-=Delta
    if pressed[pygame.K_RIGHT]:
        x+=Delta
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()
    clock.tick(10)
