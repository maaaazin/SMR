import pygame 

# Initializing pygame
pygame.init()

# This bit creates the screen of [height x width] pixels
screen = pygame.display.set_mode((800,600))

# The title and icon for the game
pygame.display.set_caption("SMR")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# Event is anything that happens inside the game window

# This is an infinte loop that makes sure window keeps running 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,255,0)) # These are RGB values. bound - {0,255}. Stored in tuples
    pygame.display.update()