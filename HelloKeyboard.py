import pygame
from pygame.locals import *

pygame.init()
# make a variable and save the display mode in it
screen = pygame.display.set_mode((500, 500), 0, 32)
sprite1 = pygame.image.load('./Images/butterfly.png')
sprite1 =pygame.transform.scale(sprite1,(32,32))
spriteWidth = sprite1.get_width()
spriteHeight = sprite1.get_height()
# set the caption for display
pygame.display.set_caption('Hello Sprite')
screen.fill((0, 0, 0))
# a program which required to open a window must run a loop until the window is closed called main game loop
game_over = False
x, y=(0,0)
#setting the frame so that the game run on the same speed on all systems
clock = pygame.time.Clock()
# main game loop
while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            x, y =event.pos
            x-=spriteWidth/2
            y-=spriteHeight/2
        pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y-=0.5 * dt
    if pressed[K_DOWN]:
        y+=0.5 * dt
    if pressed[K_LEFT]:
        x-=0.5 * dt
    if pressed[K_RIGHT]:
        x+=0.5 * dt
    if pressed[K_SPACE]:
        x=0
        y=0
    if x > (screen.get_width() - spriteWidth):
        x = screen.get_width() - spriteWidth
    if y> (screen.get_height() - spriteHeight):
        y = screen.get_height() - spriteHeight
    if x < 0:
        x=0
    if y < 0:
        y=0
    screen.fill((0, 0, 0)) #Clear screnn before drawing something new
    screen.blit(sprite1, (x,y) )#blit is used to draw the objects on the main screen
    pygame.display.update() #refresh the screen
pygame.quit()
