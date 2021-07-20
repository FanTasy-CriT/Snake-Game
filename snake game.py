import pygame
import time
from pygame import draw
from pygame.locals import *
import random
pygame.init()
game_window = pygame.display.set_mode(size=(1000,500))
# Giving my screen a color
game_window.fill((255,255,255))
def update_player_move(block_x,block_y):
    game_window.fill((255,255,255))
    rectangle = pygame.Rect(block_x,block_y,15, 15)
    pygame.draw.rect(game_window, (175,0,42), rectangle)
    pygame.display.update()
    
    pass
def draw_food():
    rectangle = pygame.Rect(random.randint(15,1000), random.randint(15,500),15, 15)
    pygame.draw.rect(game_window, (175,0,42), rectangle)
    # Update our display
    pygame.display.update()
draw_food()
game_running=True
# Game loop
block_x = 300
block_y= 100
while game_running:
    rectangle = pygame.Rect(block_x,block_y,15, 15)
    pygame.draw.rect(game_window, (175,0,42), rectangle)
    # Update our display
    pygame.display.update()
    # Loop through all active events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
        #all arrows moves
            if event.type == pygame.QUIT:
                game_running = False
            if event.key == K_UP:
                block_y -= 10
            if event.key == K_DOWN:
                block_y += 10
            if event.key == K_LEFT:
                block_x -= 10
            if event.key == K_RIGHT:
                block_x +=10
            update_player_move(block_x,block_y)
        # Close the program if the user presses the 'X'
        elif event.type == pygame.QUIT:
            game_running = False


time.sleep(5)