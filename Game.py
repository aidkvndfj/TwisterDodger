##############################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~ Created By: Eric ~~~~~#
#~~~~ Date: May, 9, 2019 ~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
##############################

#~~~~~~~~~~~ Setup ~~~~~~~~~~~#
# Needed Imports
import pygame
import random
import sys
import Eric_Dumb_Module as edm
import time

# Class Imports
sys.path.insert(0, 'Classes')
from DebrisClass import *
from PlayerClass import *
from TornadoClass import *

# Constants
global WIDTH, HEIGHT, FPS
WIDTH = 1024
HEIGHT = 576
FPS = 30

# Define Colors
BACKGROUND = (160, 145, 250)
RED        = (255, 0, 0)
GRASS      = (40, 120, 20)
GROUND     = (120, 70, 20)

# Variables
global groundHeight
groundHeight = 120

# Initialization
pygame.init()
pygame.font.init()

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Twister Dodger")

# Clock Setup
clock = pygame.time.Clock()

# Font Setup

#~~~~~~~~~ Functions ~~~~~~~~~#
def spawnDebris():
    global WIDTH, HEIGHT, groundHeight
    chance = random.randint(1, 12)
    if (chance == 5):
        debris = Debris(WIDTH, HEIGHT)
        debrisSprites.add(debris)

def drawGround():
    global WIDTH, groundHeight
    pygame.draw.rect(screen, GROUND, (0, HEIGHT - groundHeight, WIDTH, groundHeight))
    pygame.draw.rect(screen, GRASS, (0, HEIGHT - groundHeight, WIDTH, 50))

def Game():
    start = time.time()
    global groundHeight, FPS
    #~~~~~~~~ Sprite Init ~~~~~~~~#
    # Sprite Groups
    global debrisSprites
    allSprites = pygame.sprite.Group()
    debrisSprites = pygame.sprite.Group()

    # Sprites
    player = Player(WIDTH, HEIGHT, groundHeight)
    tornado = Tornado(WIDTH, HEIGHT)
    allSprites.add(player, tornado)

    running = True
    while (running):
        clock.tick(FPS)

        # Sprite Collision / Damage Player
        if (player.health <= 0):
            running = False
        if(pygame.sprite.spritecollide(player, debrisSprites, True)):
            player.GetHit()
        if (player.rect.x > 600):
            player.drainHP()
        else:
            player.regenHP()

        # Game events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # If the 'X' in the corner is clicked exit
                running = False
            if (event.type == pygame.KEYDOWN):
                key = pygame.key.get_pressed()
                if (key[pygame.K_SPACE]):
                    player.Jump()

        # Spawn Debris
        spawnDebris()

        # Update Sprites
        allSprites.update()
        debrisSprites.update()

        # Draw Frame
        screen.fill(BACKGROUND)
        debrisSprites.draw(screen)
        drawGround()
        allSprites.draw(screen)
        pygame.draw.rect(screen, RED, (10, 10, player.health * 4, 30))

        pygame.display.flip()

    pygame.font.quit()
    pygame.quit()
    end = time.time()
    return end - start
