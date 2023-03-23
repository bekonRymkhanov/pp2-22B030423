import pygame
import os
pygame.mixer.init(44100, -16, 2, 4096)
screen=pygame.display.set_mode((500,500))
runned=True
clock=pygame.time.Clock()
print(pygame.mixer.get_busy())
while runned:
    screen.fill((0,0,0))
    buttonnext=pygame.key.get_pressed()
    if buttonnext[pygame.K_SPACE]:
        a=pygame.mixer.music.load('C:/Users/User/Desktop/python/music/somthing.mp3')
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
    pygame.display.flip()