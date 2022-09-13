import pygame

pygame.init()
# make a variable and save the display mode in it
screen = pygame.display.set_mode((800, 600), 0, 32)
sprite1 = pygame.image.load('./Images/football.png')
# set the caption for display
pygame.display.set_caption('Hello Sprite')
screen.fill((0, 0, 0))
# a program which required to open a window must run a loop until the window is closed called main game loop
game_over = False
# main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (384,284)) #blit is used to draw the objects on the main screen
    pygame.display.update() #refresh the screen
pygame.quit()
