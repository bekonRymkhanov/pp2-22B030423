import pygame
import random
pygame.init()
pygame.mixer.init()
#function that draws lines
def drawlines(screen,HEIGHT,WIDTH,block):
    for i in range (0,HEIGHT+block,block):
        pygame.draw.line(screen,(255,255,255),(i,0),(i,WIDTH),1)
    for i in range (0,WIDTH+block,block):
        pygame.draw.line(screen,(255,255,255),(0,i),(HEIGHT,i),1)

class Point:  #function that allows us to initialize that in list we have not tuple,we have something that can be taken out by smth.x and smth.y
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Snake:  
    snakebody=[] 
    def __init__(self):
        self.snakebody=[(Point(x=HEIGHT//2//BLOCK,y=WIDTH//2//BLOCK))] #initialize start position

    def draw(self):
        head=self.snakebody[0] #first block in list is head
        pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(head.x*BLOCK,head.y*BLOCK,BLOCK,BLOCK)) #draw
        for body in self.snakebody[1:]: #draw body,but start not from 0 ,start from 1
            pygame.draw.rect(SCREEN,(0,200,100),pygame.Rect(body.x*BLOCK,body.y*BLOCK,BLOCK,BLOCK))

    def move(self,dx,dy):
        for inx in range(len(self.snakebody)-1,0,-1):# change cordinates to the cordinates of previous in the list
            self.snakebody[inx].x=self.snakebody[inx-1].x
            self.snakebody[inx].y=self.snakebody[inx-1].y
        self.snakebody[0].x+=dx
        self.snakebody[0].y+=dy
        if self.snakebody[0].x>=HEIGHT//BLOCK:
            self.snakebody[0].x=0
        elif self.snakebody[0].x<0:
            self.snakebody[0].x=HEIGHT//BLOCK
        elif self.snakebody[0].y>=WIDTH//BLOCK:
            self.snakebody[0].y=0
        elif self.snakebody[0].y<0:
            self.snakebody[0].y=WIDTH//BLOCK

    def collision(self,foodx,foody): # checing colision with head of snake ond x,y cords
        if foodx==self.snakebody[0].x and foody==self.snakebody[0].y:
            return True
        return False

class Bomb:
    def __init__(self):
        self.x=random.randint(0,HEIGHT//BLOCK-1)
        self.y=random.randint(0,WIDTH//BLOCK-1)
    def draw(self):
        pygame.draw.circle(SCREEN,(150,255,255),(self.x*BLOCK+BLOCK//2,self.y*BLOCK+BLOCK//2),BLOCK//2)

class Food: #food.
    def __init__(self):
        self.x=random.randint(0,HEIGHT//BLOCK-1)
        self.y=random.randint(0,WIDTH//BLOCK-1)

    def draw(self):
        pygame.draw.circle(SCREEN,(200,0,0),(self.x*BLOCK+BLOCK//2,self.y*BLOCK+BLOCK//2),BLOCK//2)

class Walls:
    def __init__(self) -> None:
        self.x=0
        self.y=0
        self.wall_list=[Point(x=0,y=0)]
    def draw(self):
        for i in range(0,WIDTH,BLOCK):  
            pygame.draw.rect(SCREEN,(200,200,200),pygame.Rect(self.x,i,BLOCK-5,BLOCK-5))
            self.wall_list.append(Point(self.x,i/BLOCK))

runned=True
WIDTH,HEIGHT,BLOCK=700,700,50
clock=pygame.time.Clock()
dx,dy=0,0
x=5
level=1
saved_lenght=0
SCREEN=pygame.display.set_mode((HEIGHT,WIDTH),pygame.RESIZABLE)
all_font=pygame.font.SysFont("Italic",50)
music_bomb=pygame.mixer.Sound("C:/Users/User/Desktop/python/music/crash.mp3")
music_apple=pygame.mixer.Sound("C:/Users/User/Desktop/python/music/Apple_Bite-Simon_Craggs-1683647397.mp3")
snake=Snake()
food=Food()
walls=Walls()
bomb=Bomb()
while runned:
    SCREEN.fill((0,0,0))
    drawlines(SCREEN,HEIGHT,WIDTH,BLOCK)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runned=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                dx,dy=0,-1
            elif event.key==pygame.K_RIGHT:
                dx,dy=1,0
            elif event.key==pygame.K_LEFT:
                dx,dy=-1,0
            elif event.key==pygame.K_DOWN:
                dx,dy=0,1
    snake.move(dx,dy)
    food.draw()
    for i in range(1,len(snake.snakebody)):
        if snake.collision(snake.snakebody[i].x,snake.snakebody[i].y):
            runned=False
    snake.draw()
    walls.draw()
    bomb.draw()
    level_see=all_font.render(f"level: {level}",True,(255,255,255))
    score_see=all_font.render(f"score: {len(snake.snakebody)}",True,(255,255,255))
    font = pygame.font.SysFont("Verdana", 60)
    font2 = pygame.font.SysFont("Verdana", 60)
    button=font2.render("exit",True,(200,200,0))
    game_over = font.render("Game Over", True, (0,0,0))
    SCREEN.blit(level_see,(0,0))
    SCREEN.blit(score_see,(HEIGHT-150,0))

    if snake.collision(food.x,food.y):
        music_apple.play()
        snake.snakebody.append(Point(food.x,food.y))
        food.x=random.randint(0,HEIGHT//BLOCK-1)
        food.y=random.randint(0,WIDTH//BLOCK-1)
        for i in range(len(walls.wall_list)):
            for j in range(len(snake.snakebody)):
                if (snake.snakebody[j].x==food.x and snake.snakebody[j].y==food.y)or (walls.wall_list[i].x==food.x or walls.wall_list[i].y==food.y):
                    food.x=random.randint(0,HEIGHT//BLOCK-1)
                    food.y=random.randint(0,WIDTH//BLOCK-1)
    if snake.collision(bomb.x,bomb.y):
        music_bomb.play()
        snake.snakebody.pop()
        while len(snake.snakebody)==0:
            SCREEN.fill((255,0,0))
            SCREEN.blit(game_over, SCREEN.get_rect().center)
            pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(200,200,50,50),0)
            #SCREEN.blit(SCREEN)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0]>200 and pygame.mouse.get_pos()[0]<250) and (pygame.mouse.get_pos()[1]>200 and pygame.mouse.get_pos()[1]<250) :
                    pygame.quit()
                if event.type==pygame.QUIT:
                    pygame.quit()

        bomb.x=random.randint(0,HEIGHT//BLOCK-1)
        bomb.y=random.randint(0,WIDTH//BLOCK-1)
        for i in range(len(walls.wall_list)):
            for j in range(len(snake.snakebody)):
                if (snake.snakebody[j].x==bomb.x and snake.snakebody[j].y==bomb.y)or (walls.wall_list[i].x==bomb.x or walls.wall_list[i].y==bomb.y):
                    bomb.x=random.randint(0,HEIGHT//BLOCK-1)
                    bomb.y=random.randint(0,WIDTH//BLOCK-1)

    for i in range(len(walls.wall_list)):
        if snake.collision(walls.wall_list[i].x,walls.wall_list[i].y):
            music_bomb.play()
            while 1:
                SCREEN.fill((255,0,0))
                SCREEN.blit(game_over, SCREEN.get_rect().center)
                SCREEN.blit(button,(200,200))
                pygame.draw.rect(SCREEN,(0,255,0),pygame.Rect(200,200,50,50),0)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN and (pygame.mouse.get_pos()[0]>200 and pygame.mouse.get_pos()[0]<250) and (pygame.mouse.get_pos()[1]>200 and pygame.mouse.get_pos()[1]<250) :
                        pygame.quit()
                    if event.type==pygame.QUIT:
                        pygame.quit()


    if len(snake.snakebody)%5==0 and saved_lenght!=len(snake.snakebody):
        x+=1
        saved_lenght=len(snake.snakebody)
        level+=1
    
    pygame.display.flip()
    clock.tick(x)
