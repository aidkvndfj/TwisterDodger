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
WDITH = 1024
HEIGHT = 576
FPS = 30

# Define Colors
BACKGROUND = (25, 25, 80)

# Variables
global groundHeight
groundHeight = 100

# Initialization
pygame.init()
pygame.font.init()

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Twister Dodger")

# Clock Setup
clock = pygame.time.Clock()

# Font Setup

def Game():
    global groundHeight
    #~~~~~~~~ Sprite Init ~~~~~~~~#
    # Sprite Groups
    allSprites = pygame.sprite.Group()
    debrisSprites = pygame.sprite.Group()

    # Sprites
    player = Player(WIDTH, HEIGHT, groundHeight)
