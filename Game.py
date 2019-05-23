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
from CloudClass import *

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
    global groundHeight, spawnGrass, grassX, grassY
    groundHeight = 120
    gameTime = 0
    spawnGrass = False
    grassX = []
    grassY = []

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
    verNum = gameFont.render("V4.0.2", True, (255, 255, 255))

    #~~~~~~~~~ Functions ~~~~~~~~~#
    def spawnDebris(difficulty):
        global WIDTH, HEIGHT, groundHeight
        chance = random.randint(1, 350)
        powerChance = random.randint(1, 500)
        if (chance < difficulty):
            debris = Debris(WIDTH, HEIGHT)
            debrisSprites.add(debris)
        # chance = 57
        if (powerChance == 45 and player.hasHelmet == False):
            helmet = Helmet(WIDTH, HEIGHT)
            powerSprites.add(helmet)
        if (powerChance == 57 and player.hasFuelcell == False):
            fuelcell = Fuelcell(WIDTH, HEIGHT)
            powerSprites.add(fuelcell)


    def drawGround():
        global WIDTH, HEIGHT, groundHeight, spawnGrass, grassX, grassY
        pygame.draw.rect(screen, GROUND, (0, HEIGHT - groundHeight, WIDTH, groundHeight))
        pygame.draw.rect(screen, GRASS, (0, HEIGHT - groundHeight, WIDTH, 30))
        if (spawnGrass == False):
            for i in range(1, (groundHeight - 30) / 5):
                for j in range(0, WIDTH, 5):
                    newGrass = random.randint(0, i)
                    if (newGrass == 1):
                        grassX.append(j)
                        grassY.append(HEIGHT - groundHeight + 25 + (i * 5))
            spawnGrass = True
        for i in range(len(grassX)):
            pygame.draw.rect(screen, GRASS, (grassX[i], grassY[i], 5, 5))


    start = time.time()
    #~~~~~~~~ Sprite Init ~~~~~~~~#
    # Sprite Groups
    global debrisSprites
    allSprites = pygame.sprite.Group()
    debrisSprites = pygame.sprite.Group()
    powerSprites = pygame.sprite.Group()
    cloudSprites = pygame.sprite.Group()

    # Sprites
    player = Player(WIDTH, HEIGHT, groundHeight)
    tornado = Tornado(WIDTH, HEIGHT)
    fire = Fire(WIDTH, HEIGHT, groundHeight)
    cloud = Cloud(WIDTH, HEIGHT)
    cloud2 = Cloud(WIDTH, HEIGHT)
    cloud3 = Cloud(WIDTH, HEIGHT)

    allSprites.add(player, tornado, fire)
    cloudSprites.add(cloud, cloud2, cloud3)

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

        end = time.time()
        gameTime = (end - start)

        # Game events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # If the 'X' in the corner is clicked exit
                running = False

        # Spawn Debris
        gameDifficulty = (4 * (1.014 ** (end - start)) + 21)
        spawnDebris(gameDifficulty)

        # Update Text
        difficultyText = gameFont.render("Dificulty: {0:0.1f}".format(gameDifficulty), True, (255, 255, 255))
        timeText = gameFont.render("Time: {0:0.1f}".format(gameTime), True, (255, 255, 255))
        # Update Sprites
        allSprites.update()
        debrisSprites.update()
        powerSprites.update()
        cloudSprites.update()
        fire.updateFire(player.rect.x, player.rect.y, player.rect.width, player.rect.height, player.playerFlying)

        # Draw Frame100
        screen.fill(BACKGROUND)
        # Draw the clouds
        cloudSprites.draw(screen)
        # Draw fuel and health bars
        pygame.draw.rect(screen, RED, (10, 30, player.health * 4, 30)) # Health Bar
        pygame.draw.rect(screen, FUEL, (10, 80, player.fuel * 2.5, 15)) # Fuel Bar
        # Draw the subtitle texts
        screen.blit(healthText, (10, 10)) # The health
        screen.blit(fuelText, (10, 65)) # The fuel
        # Draw sprites
        debrisSprites.draw(screen) # All the rocks
        powerSprites.draw(screen) # All the power-ups
        allSprites.draw(screen) # the player and tornado
        # Draw the ground
        drawGround() # The ground
        # Draw the info texts
        screen.blit(timeText, (WIDTH - 95, HEIGHT - 25)) # The time in the corner
        screen.blit(difficultyText, (WIDTH - 250, HEIGHT - 25)) # The difficulty in the corner
        screen.blit(verNum, (10, HEIGHT - 25)) # The version number

        # Display the new frame
        pygame.display.flip()

    pygame.font.quit()
    pygame.quit()
    return gameTime
