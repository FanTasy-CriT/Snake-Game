from typing_extensions import runtime
import pygame
import time
from pygame import draw
from pygame.locals import *
import random
pygame.init()
game_window = pygame.display.set_mode(size=(1000,500))
# Giving my screen a color
game_window.fill((255,255,255))
def update_player_move(block_x,block_y,z=15):
    game_window.fill((255,255,255))
    rectangle = pygame.Rect(block_x,block_y,15, 15)
    pygame.draw.rect(game_window, (175,0,42), rectangle)
    pygame.display.update()
    
    pass
def draw_food(x,y):
    rectangle = pygame.Rect(x,y,15, 15)
    pygame.draw.rect(game_window, (175,0,42), rectangle)
    # Update our display
    pygame.display.update()
game_running=True
# Game loop
x=2
y=2
while(x%15!=0 or y%15!=0):
    x=random.randint(1,1000)
    y=random.randint(1,500)
block_x = 300
block_y= 100
draw_food(x,y)
while game_running:
    rectangle = pygame.Rect(block_x,block_y,15, 15)
    pygame.draw.rect(game_window, (0,0,0), rectangle)
    # Update our display
    pygame.display.update()
    # Loop through all active events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
        #all arrows moves
            if event.type == pygame.QUIT:
                game_running = False
            if event.key == K_UP:
                block_y -= 15
            if event.key == K_DOWN:
                block_y += 15
            if event.key == K_LEFT:
                block_x -= 15
            if event.key == K_RIGHT:
                block_x +=15
            update_player_move(block_x,block_y)
            draw_food(x,y)
        # Close the program if the user presses the 'X'
            if(block_x<0 or block_y<0):
                game_running=False
                print('Game Over: You Hit a wall')
        elif event.type == pygame.QUIT:
            game_running = False
            print('Left The Game')
