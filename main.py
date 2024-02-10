import pygame as pg

# Initializing pygame
pg.init()

# This bit creates the screen of [height x width] pixels
screen = pg.display.set_mode((800,600))

# The title and icon for the game
pg.display.set_caption("SMR")
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

# Player
player_img = pg.image.load('spaceship.png')
playerX = 370
playerY = 480

def player():
    screen.blit(player_img, (playerX, playerY))

# This is an infinte loop that makes sure window keeps running 
running = True
while running:

    screen.fill((0,0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    player()
    pg.display.update()