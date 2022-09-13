import pygame

pygame.init()
# make a variable and save the display mode in it
screen = pygame.display.set_mode((640, 480), 0, 32)
# set the caption for display
pygame.display.set_caption('Hello Pygame')
screen.fill((0, 0, 0))
# a program which required to open a window must run a loop untill the window is closed
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True
pygame.quit()


