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
import easygui as gui

# Class Imports
sys.path.insert(0, 'Classes')
from DebrisClass import *
from PlayerClass import *
from TornadoClass import *
from FireClass import *
# from HelmetPower import *
# from FuelcellPower import *
from PowerupClasses import *

def Game():
    # Constants
    global WIDTH, HEIGHT, FPS
    WIDTH = 1024
    HEIGHT = 576
    FPS = 30

    # Define Colors
    BACKGROUND           = (160, 145, 250)
    RED                  = (255, 0, 0)
    GRASS                = (40, 120, 20)
    GROUND               = (120, 70, 20)
    FUEL                 = (255, 200, 50)

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
    gameFont = pygame.font.Font(None, 25)
    fuelFont = pygame.font.Font(None, 20)
    healthText = gameFont.render("Health:", True, (0, 0, 0))
    fuelText = fuelFont.render("Fuel:", True, (0, 0, 0))

    #~~~~~~~~~ Functions ~~~~~~~~~#
    def spawnDebris():
        global WIDTH, HEIGHT, groundHeight
        chance = random.randint(1, 100)
        if (chance < 15):
            debris = Debris(WIDTH, HEIGHT)
            debrisSprites.add(debris)
        # chance = 57
        if (chance == 45 and player.hasHelmet == False):
            helmet = Helmet(WIDTH, HEIGHT)
            powerSprites.add(helmet)
        if (chance == 57 and player.hasFuelcell == False):
            fuelcell = Fuelcell(WIDTH, HEIGHT)
            powerSprites.add(fuelcell)


    def drawGround():
        global WIDTH, groundHeight
        pygame.draw.rect(screen, GROUND, (0, HEIGHT - groundHeight, WIDTH, groundHeight))
        pygame.draw.rect(screen, GRASS, (0, HEIGHT - groundHeight, WIDTH, 50))


    start = time.time()
    #~~~~~~~~ Sprite Init ~~~~~~~~#
    # Sprite Groups
    global debrisSprites
    allSprites = pygame.sprite.Group()
    debrisSprites = pygame.sprite.Group()
    powerSprites = pygame.sprite.Group()

    # Sprites
    player = Player(WIDTH, HEIGHT, groundHeight)
    tornado = Tornado(WIDTH, HEIGHT)
    fire = Fire(WIDTH, HEIGHT, groundHeight)
    allSprites.add(player, tornado, fire)

    running = True
    while (running):
        clock.tick(FPS)

        # Sprite Collision / Damage Player
        if (player.health <= 0):
            running = False
        if (pygame.sprite.spritecollide(player, debrisSprites, True)):
            player.GetHit()
        powerUp = pygame.sprite.spritecollideany(player, powerSprites)
        if (powerUp != None):
            type = powerUp.Collected()
            if (type == "Helmet"):
                player.GetHelmet()
            if (type == "Fuelcell"):
                player.GetFuelcell()

        # Game events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # If the 'X' in the corner is clicked exit
                running = False

        # Spawn Debris
        spawnDebris()

        # Update Sprites
        allSprites.update()
        debrisSprites.update()
        powerSprites.update()
        fire.updateFire(player.rect.x, player.rect.y, player.rect.width, player.rect.height)
        # Update Text
        end = time.time()
        timeText = gameFont.render("Time: {0:0.1f}".format(end - start), True, (255, 255, 255))

        # Draw Frame
        screen.fill(BACKGROUND)
        pygame.draw.rect(screen, RED, (10, 30, player.health * 4, 30))
        pygame.draw.rect(screen, FUEL, (10, 80, player.fuel * 2.5, 15))
        debrisSprites.draw(screen)
        powerSprites.draw(screen)
        drawGround()
        allSprites.draw(screen)
        screen.blit(healthText, (10, 10))
        screen.blit(fuelText, (10, 65))
        screen.blit(timeText, (WIDTH - 95, HEIGHT - 25))

        pygame.display.flip()

    pygame.font.quit()
    pygame.quit()
    return end - start
