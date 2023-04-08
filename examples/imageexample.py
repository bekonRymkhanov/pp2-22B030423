import pygame
pygame.init()
screen=pygame.display.set_mode((1366,740))
pygame.display.set_caption("hello")
image=pygame.image.load('C:/Users/User/Desktop/python/images/YELAN.png')
resizedimage=pygame.transform.scale(image,(708,370))
clock=pygame.time.Clock()
running=True
x,y,dx,dy,Delta=50,50,0,0,10
while running:
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT]:
        dx=-Delta
        dy=Delta
    elif pressed[pygame.K_LEFT] and pressed[pygame.K_UP]:
        dx=-Delta
        dy=-Delta
    elif pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]:
        dx=Delta
        dy=-Delta
    elif pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]:
        dx=Delta
        dy=Delta
    elif pressed[pygame.K_UP]:
        dy=-Delta
    elif pressed[pygame.K_DOWN]:
        dy=Delta
    elif pressed[pygame.K_LEFT]:
        dx=-Delta
    elif pressed[pygame.K_RIGHT]:
        dx=Delta
    else:
        dx=0
        dy=0
    x=x+dx
    y=y+dy
    screen.fill((255,255,255))
    screen.blit(resizedimage,(x,y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()
    clock.tick(60)