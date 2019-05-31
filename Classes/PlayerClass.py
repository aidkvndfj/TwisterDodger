import pygame
import os
import sys
sys.path.insert(0, './Dependencies')
import Eric_Dumb_Module as edm

# Setup Images
gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')
playerImage = pygame.image.load(os.path.join(imgFolder, 'Player.png'))
playerWithHelmetImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithHelmet.png'))
playerWithRocketbootsImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithRocketboots.png'))
playerWithRocketbootsAndHelmetImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithRocketbootsAndHelmet.png'))
playerWithFuelRegeneratorImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithFuelRegenerator.png'))
playerWithFuelRegeneratorAndHelmetImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithFuelRegeneratorAndHelmet.png'))
playerWithFastFuelRegeneratorImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithFastFuelRegenerator.png'))
playerWithFastFuelRegeneratorAndHelmetImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithFastFuelRegeneratorAndHelmet.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, GROUNDHEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImage # Sets the default image of the player to the player looking right
        self.rect = self.image.get_rect() # Sets the rect box of the player to the image size
        self.rect.centerx = 200 # set the center x to spawn location
        self.rect.centery = HEIGHT - GROUNDHEIGHT # set the centery to the ground

        # Screen Variables
        self.screenHeight = HEIGHT # set local screen height for use later
        self.screenWidth = WIDTH # set loacl screen width for use later
        self.groundHeight = GROUNDHEIGHT # set local ground height for use later

        # Player Movement Variables
        self.gravity = 1.5 # Gravity on the player
        self.vel = edm.Vector(10, 0) # The velocity on the player as a 2D vector
        self.airTime = 0 # The time that the player has been above the ground
        self.playerFlying = False # Wheather or not the player is flying

        # Player Stat Varibales
        self.health = 100 # The starting health
        self.maxHealth = 100 # The starting max health
        self.fuel = 100 # The starting fuel of the player
        self.maxFuel = 100 # The starting maximum fuel
        self.debrisDamage = 34 # The starting damage that the debris will do to the player

        # Player Equipment Variables
        self.hasHelmet = False # Weather or not the player has the helmet (Player starts without it)
        self.hasRocketboots = False # Weather or not the player has the Rocket boots (Player starts without it)
        self.hasFuelRegenerator = False # Weather or not the player has the fuel regen upgrade (Player starts without it)
        self.hasFastFuelRegenerator = False# Weather or not the player has the fast fuel regen upgrade (Player starts without it)
        self.hasBigFuelcell = False # Weather or not the player has the big fuel cell (Player starts without it)

        # Player Timer Variables
        self.healthRegenWaitTimer = 0 # The wait timer for regenerating health
        self.fuelRegenWaitTimer = 0 # The wait timer for regenerating fuel

# ~~~~~ Standard Update Function ~~~~~ #
    def update(self):
        key = pygame.key.get_pressed() # the most recent key pressed

        if (key[pygame.K_SPACE]): # if the space key is pressed
            if (self.IsGrounded()): # If the player is on the ground, jump and set flying to false
                self.PlayerJump()
                self.playerFlying = False
            elif (self.airTime > 0.5 and self.fuel > 0 and self.hasRocketboots == True): # If the player has been in the air for more than 0.5 units, and has some fuel, start flying and set variable to true
                self.PlayerFly()
                self.playerFlying = True

        self.PlayerWalk(key) # Call the walk function
        self.PlayerFall() # Call the fall function
        self.PlayerRegenHealth() # Call the health regen function
        self.PlayerRegenFuel() # Call the fuel regen function

        # Cheats
        if (key[pygame.K_w]): # If 'w' key is pressed than set the limit and fuel to 10000
            self.fuelLimit = 10000
            self.fuel = 10000
        if (key[pygame.K_e]): # If 'e' key is pressed than set the damage to 0
            self.debrisDamage = 0

# ~~~~~ Stat Functions ~~~~~ #
    def PlayerHit(self): # gets called if the player gets hit by debris
        self.health -= self.debrisDamage # Removes the debris damage from the players health
        self.healthRegenWaitTimer = 5 # set the health regen wait timer to 5

    def PlayerRegenHealth(self):
        if (self.airTime <= 0 and self.healthRegenWaitTimer <= 0 and self.health < self.maxHealth): # if the player is on the ground and the timer is 0 and the player isn't at max health
            self.health += 1 # add 1 to current health
        elif (self.airTime > 0): # if player is not on the ground
            self.healthRegenWaitTimer = self.healthRegenWaitTimer # Don't change the timer
        elif (self.healthRegenWaitTimer >= 0): # if the timer is not at 0
            self.healthRegenWaitTimer -= 0.1 # takeaway 0.1 from the timer

    def PlayerRegenFuel(self):
        if (self.airTime <= 0 and self.fuelRegenWaitTimer <= 0 and self.fuel < self.maxFuel): # if the player is on the ground and the timer is 0 and the player isn't at max fuel
            if (self.hasFastFuelRegenerator): # if the player has fast fuel regen
                self.fuel += 1 # adds 1 to current fuel
            elif (self.hasFuelRegenerator == True): # else if player has normal fuel regen
                self.fuel += 0.5 # add 0.5 to current fuel
            else: # otherwise
                self.fuel = self.fuel # keep the fuel the same number
        elif (self.airTime > 0): # if player is not on the ground
            if (self.hasFastFuelRegenerator == True): # if the player has fast fuel regen
                self.fuelRegenWaitTimer = 3 # set the timer to 3
            else: # otherwise
                self.fuelRegenWaitTimer = 5 # set the timer to 5
        elif (self.fuelRegenWaitTimer >= 0): # if the timer is not at 0
            self.fuelRegenWaitTimer -= 0.1 # takeaway 0.1 from the timer

# ~~~~~ Equipment Functions ~~~~~ #
    def CollectHelmet(self): # gets called if the player runs into a helmet powerup
        self.hasHelmet = True # set the has helmet var to true meaning the player has the helmet
        self.debrisDamage = 25 # changes the debris damage to 25, making it 4 hits from full to die

    def CollectBigFuelcell(self): # gets called if the player runs into a big fuellcell powerup
        self.hasBigFuelcell = True # sets the has big fuelcell var to true meaning the plyaer has the big fuel cell
        self.maxFuel = 200 # changs the max fuel to 200
        self.fuel = self.maxFuel # set the players fuel to the new max fuel

    def CollectFuelRegenerator(self): # gets called if the player runs into a fuel regenerator poweurp
        self.hasFuelRegenerator = True # Sets the has fuel regenerator var to true meaning the player has the fuel regenerator

    def CollectFastFuelRegenerator(self): # gets called if the player runs into a fast fuel regenerator poweurp
        self.hasFastFuelRegenerator = True # Sets the has fast fuel regenerator var to true meaning the player has the fuel regenerator

    def CollectRocketboots(self):
        self.hasRocketboots = True

    def CollectFuelPickup(self):
        self.fuel += 10
        if (self.fuel > 100):
            self.fuel = 100

# ~~~~~ Movement Functions ~~~~~ #
    def PlayerWalk(self, key):
        if (key[pygame.K_LEFT]): # If the left key is pressed, remove x vel, subtract 2 because player is running from the tornado, from current pos
            self.rect.x -= self.vel.x - 2
            self.PlayerLookLeft() # Changes the sprite to look to the left

        if (key[pygame.K_RIGHT]): # If the right key is pressed, add x vel, plus 2 because player is running toawrd the tornado, from current pos
            self.rect.x += self.vel.x + 2
            self.PlayerLookRight() # Changes the sprite to look to the right

        if (self.rect.x < 0): # if the player is past the left side of the screen, set the pos to the left side of the screen
            self.rect.x = 0

        if (self.rect.x > 750): # if the player in the tornado, move the players pos to outside the tornado.
            self.rect.x = 750

        if (self.rect.x > 700): # if the player is close to the tornado, take away health slowly
            self.health -= 1

    def PlayerJump(self):
        self.vel.y = -13 # set the y velocity to -13

    def PlayerFly(self):
        if (self.rect.top < 0): # If the player is at the top of the screen
            self.rect.top = 0 # set the top of the player to 0, a.k.a the top of the screen
            self.vel.y = 0 # set the players velocity to 0
            self.vel.y -= self.gravity # take away gravity so that the player doesn't bounce on the top of the screen.
        elif (self.vel.y >= 0): # if the player is falling, have the upwards boost greater for a more fun experience
            self.vel.y -= 3 # subtract 3 from the velocity so that the player flys upwards.
        else:
            self.vel.y -= 2 # subtract 2 from the velocity so that the player flys upwards.

        self.fuel -= 1 # take away 1 from the current fuel.

    def PlayerFall(self):
        self.rect.y += self.vel.y # add the y vel to the current y pos, moving the character down if posative or up is negative

        if (self.rect.bottom > self.screenHeight - self.groundHeight): # if the bottom of the player is lower than the ground
            self.rect.bottom = self.screenHeight - self.groundHeight # set the bototm of the player to the ground
            self.vel.y = 0 # set the velocity to 0
        else: # Otherwise, add the gravity to the y vel
            self.vel.y += self.gravity

        if (self.IsGrounded() == False): # if the player is not touching the ground
            self.airTime += 0.1 # add 0.1 to the air time
        else: # Otherwise set the air time to 0
            self.airTime = 0


# ~~~~~ Check/Getter Functions ~~~~~ #
    def IsGrounded(self):
        # if the bototm of the palyer is within a small range just above and bellow the ground, than they player is considered grounded
        if (self.rect.bottom < self.screenHeight - self.groundHeight  + 5 and self.rect.bottom > self.screenHeight - self.groundHeight - 5):
            return True
        else: # if not within that range, the player is not grounded
            return False

    def GetHelmet(self):
        return self.hasHelmet # returns the current state of the has helmet var

    def GetBigFuelcell(self):
        return self.hasBigFuelcell # returns the current state of the has big fuel cell var

    def GetFuelRegenerator(self):
        return self.hasFuelRegenerator # returns the current state of the has fuel rengerator var

    def GetFastFuelRegenerator(self):
        return self.hasFastFuelRegenerator # returns the current state of the has fast fuel rengerator var

    def GetRocketboots(self):
        return self.hasRocketboots # returns the current state of the has Rocket Boots var


# ~~~~~ Sprite Image Change Functions ~~~~~ #
    def PlayerLookRight(self):
        if (self.hasFastFuelRegenerator and self.hasHelmet):
            self.image = playerWithFastFuelRegeneratorAndHelmetImage
        elif (self.hasFastFuelRegenerator):
            self.image = playerWithFastFuelRegeneratorImage
        elif (self.hasFuelRegenerator and self.hasHelmet):
            self.image = playerWithFuelRegeneratorAndHelmetImage
        elif (self.hasFuelRegenerator):
            self.image = playerWithFuelRegeneratorImage
        elif (self.hasRocketboots and self.hasHelmet):
            self.image = playerWithRocketbootsAndHelmetImage
        elif (self.hasRocketboots):
            self.image = playerWithRocketbootsImage
        elif (self.hasHelmet):
            self.image = playerWithHelmetImage
        else: # Default to no equipment
            self.image = playerImage # set the image to looking right

    def PlayerLookLeft(self):
        if (self.hasFastFuelRegenerator and self.hasHelmet):
            self.image = pygame.transform.flip(playerWithFastFuelRegeneratorAndHelmetImage, True, False)
        elif (self.hasFastFuelRegenerator):
            self.image = pygame.transform.flip(playerWithFastFuelRegeneratorImage, True, False)
        elif (self.hasFuelRegenerator and self.hasHelmet):
            self.image = pygame.transform.flip(playerWithFuelRegeneratorAndHelmetImage, True, False)
        elif (self.hasFuelRegenerator):
            self.image = pygame.transform.flip(playerWithFuelRegeneratorImage, True, False)
        elif (self.hasRocketboots and self.hasHelmet):
            self.image = pygame.transform.flip(playerWithRocketbootsAndHelmetImage, True, False)
        elif (self.hasRocketboots):
            self.image = pygame.transform.flip(playerWithRocketbootsImage, True, False)
        elif (self.hasHelmet):
            self.image = pygame.transform.flip(playerWithHelmetImage, True, False)
        else: # Default to no equipment
            self.image = pygame.transform.flip(playerImage, True, False)
