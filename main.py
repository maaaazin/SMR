import pygame 

# Initializing pygame
pygame.init()

# This bit creates the screen of [height x width] pixels
screen = pygame.display.set_mode((800,600))


# Event is anything that happens inside the game window

# This is an infinte loop that makes sure window keeps running 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False