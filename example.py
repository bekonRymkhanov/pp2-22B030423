import pygame
pygame.init()
Height,Width,Radius=800, 500,100
screen=pygame.display.set_mode((Height,Width))
pygame.display.set_caption('hello NIGGERS')
runprog=True
while runprog:
    screen.fill((255,255,255))
    pygame.draw.line(
        (screen),
        (255,0,0),
        (0,0),
        (Height,Width),
        5)
    pygame.draw.line(
        (screen),
        (255,0,0),
        (Height,0),
        (0,Width),
        5)
    pygame.draw.rect(
        screen,
        (122,122,122),
        pygame.Rect(Height/2-Radius,Width/2-Radius,200,200),
        0)
    pygame.draw.circle(
        screen,
        (0,0,0),
        (Height/2,Width/2),
        Radius,)
    pygame.draw.polygon(
        screen,
        (0,0,0),
        [(Height/2-Radius,Width/2-Radius),(Height/2+Radius,Width/2-Radius),(Height/2,(Width/2-Radius)/2)],
        0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runprog=False
    pygame.display.flip()