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
    def SpawnDebris(difficulty):
        global WIDTH, HEIGHT, groundHeight
        chance = random.randint(1, 350)
        if (chance < difficulty):
            debris = Debris(WIDTH, HEIGHT)
            debrisSprites.add(debris)
        # powerChance = 45

    def SpawnPowerup(difficulty):
        difficultyModifier = int(difficulty / 2)
        chance = random.randint(1, 350 - difficultyModifier)

        if (chance == 45 and player.GetHelmet() == False): # check if the number if correct and that the player doesn't already have helmet
            helmet = Helmet(WIDTH, HEIGHT) # spawn the helmet
            powerSprites.add(helmet) # add the helmet to the sprite list

        if (chance == 78 and player.GetRocketBoots() == False): # check if the number is correct and that the player deosn't already have the rocket boots
            rocketBoots = RocketBoots(WIDTH, HEIGHT)
            powerSprites.add(rocketBoots)

        if (player.GetRocketBoots() == True): # player must have rocket boots in order to spawn the upgrades.
            if (chance == 20 and player.GetBigFuelcell() == False): # check if the number if correct and that the player doesn't already have big fuel cell
                bigFuelcell = BigFuelcell(WIDTH, HEIGHT) # spawn big fuel cell
                powerSprites.add(bigFuelcell) # add the big fuel cell to the sprite list

            if (chance == 15 and player.GetFuelRegenerator() == False): # check if the number if correct and that the player doesn't already have the fuel regenerator
                fuelRegenerator = FuelRegenerator(WIDTH, HEIGHT) # spawn fuel regenerator
                powerSprites.add(fuelRegenerator) # add the fuel regenerator to the sprite list
            elif (chance == 15 and player.GetFastFuelRegenerator() == False): # check if the number if correct and that the player doesn't already have the fast fuel regenerator (only possible is the player already has fuel regenerator)
                fastFuelRegenerator = FastFuelRegenerator(WIDTH, HEIGHT) # spawn fast fuel regenerator
                powerSprites.add(fastFuelRegenerator) # add the fast fuel regenerator to the sprite list


    def CollectPowerup(powerup): # Gets called when the powerup var is changed from "None"
        if (powerup == "Helmet"): # If the type is a helmet
            player.CollectHelmet() # give the player the helmet powerup
        elif (powerup == "RocketBoots"): # if the type is RocketBoots
            player.CollectRocketBoots() # give the player the Rocket Boots
        elif (powerup == "BigFuelcell"): # if the type is a big fuelcell
            player.CollectBigFuelcell() # give the player the big fuelcell
        elif (powerup == "FuelRegenerator"): # if the type is Fuel Regenerator
            player.CollectFuelRegenerator() # give the player the fuel regenerator
        elif (powerup == "FastFuelRegenerator"): # if the type is fast Fuel Regenerator
            player.CollectFastFuelRegenerator() # give the player the fast fuel regenerator
        else: # otherwise there is a error
            print("ERROR POWERUP TYPE NOT GIVEN OR IS INCORRECT. TYPE GIVEN '{}'".format(powerup))


    def DrawGround():
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
            player.PlayerHit()

        powerUp = pygame.sprite.spritecollideany(player, powerSprites)
        if (powerUp != None):
            CollectPowerup(powerUp.Collected())

        end = time.time()
        gameTime = (end - start)

        # Game events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): # If the 'X' in the corner is clicked exit
                running = False

        # Spawn Debris
        gameDifficulty = (4 * (1.014 ** (end - start)) + 21)
        SpawnDebris(gameDifficulty)
        SpawnPowerup(gameDifficulty)

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
        # Draw fuel and health bars/texts
        pygame.draw.rect(screen, RED, (10, 30, player.health * 4, 30)) # Health Bar
        screen.blit(healthText, (10, 10)) # The health
        if (player.GetRocketBoots() == True):
            pygame.draw.rect(screen, FUEL, (10, 80, player.fuel * 2, 15)) # Fuel Bar
            screen.blit(fuelText, (10, 65)) # The fuel
        # Draw sprites
        debrisSprites.draw(screen) # All the rocks
        powerSprites.draw(screen) # All the power-ups
        allSprites.draw(screen) # the player and tornado
        # Draw the ground
        DrawGround() # The ground
        # Draw the info texts
        screen.blit(timeText, (WIDTH - 95, HEIGHT - 25)) # The time in the corner
        screen.blit(difficultyText, (WIDTH - 250, HEIGHT - 25)) # The difficulty in the corner
        screen.blit(verNum, (10, HEIGHT - 25)) # The version number

        # Display the new frame
        pygame.display.flip()

    pygame.font.quit()
    pygame.quit()
    return gameTime
