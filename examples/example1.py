import pygame
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/User/Desktop/python/music/ayaka.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    print("hello")
while pygame.mixer.music.get_busy() == False:
    print("finished")
    break