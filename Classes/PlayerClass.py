import pygame
import os
import Eric_Dumb_Module as edm

# Setup Images
gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')
playerRightImage = pygame.image.load(os.path.join(imgFolder, 'Player-right.png'))
playerLeftImage = pygame.image.load(os.path.join(imgFolder, 'Player-left.png'))

class Player(pygame.sprite.Sprite):
    # Initalize Function
    def __init__(self, WIDTH, HEIGHT, GROUNDHEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerRightImage
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = HEIGHT - 100

        # Screen Variables
        self.screenHeight = HEIGHT
        self.screenWidth = WIDTH
        self.groundHeight = GROUNDHEIGHT

        # Player Movemenet Variables
        self.gravity = 1.5 # Gravity on the player
        self.vel = edm.Vector(10, 0) # The velocity on the player as a 2D vector
        self.airTime = 0 # The time that the player has been above the ground
        self.playerFlying = False # Wheather or not the player is flying

        # Player Stat Varibales
        self.health = 100 # The starting health
        self.maxHelath = 100 # The starting max health
        self.fuel = 100 # The starting fuel of the player
        self.maxFuel = 100 # The starting maximum fuel
        self.debrisDamage = 34 # The starting damage that the debris will do to the player

        # Player Equipment Variables
        self.hasHelmet = False # Weather or not the player has the helmet (Player starts without it)
        self.hasRocketBoots = False # Weather or not the player has the Rocket boots (Player starts without it)
        self.hasBigFuelcell = False # Weather or not the player has the big fuel cell (Player starts without it)
        self.hasFuelRegen = False # Weather or not the player has the fuel regen upgrade (Player starts without it)
        self.hasFastFuelRegen = False # Weather or not the player has the fast fuel regen upgrade (Player starts without it)

        # Player Timer Variables
        self.regenWaitTimer = 0 # The wait timer for regenerating health

    # Standard update function
    def update(self):
        key = pygame.key.get_pressed() # the most recent key pressed

        if (key[pygame.K_SPACE]): # if the space key is pressed
            if (self.IsGrounded()): # If the player is on the ground, jump and set flying to false
                self.PlayerJump()
                self.playerFlying = False
            elif (self.airTime > 0.5 and self.fuel > 0): # If the player has been in the air for more than 0.5 units, and has some fuel, start flying and set variable to true
                self.PlayerFly()
                self.playerFlying = True

        self.PlayerWalk(key) # Call the walk function
        self.PlayerFall() # Call the fall function

        # Cheats
        if (key[pygame.K_w]): # If 'w' key is pressed than set the limit and fuel to 10000
            self.fuelLimit = 10000
            self.fuel = 10000
        if (key[pygame.K_e]): # If 'e' key is pressed than set the damage to 0
            self.debrisDamage = 0

    # Stat Functions
    def PlayerHit(self):
        self.health -= self.debrisDamage

    # Movement functions
    def PlayerWalk(self, key):
        if (key[pygame.K_LEFT]): # If the left key is pressed, remove x vel, subtract 2 because player is running from the tornado, from current pos
            self.rect.x -= self.vel.x - 2
            self.image = playerLeftImage # set the image to looking left
        if (key[pygame.K_RIGHT]): # If the right key is pressed, add x vel, plus 2 because player is running toawrd the tornado, from current pos
            self.rect.x += self.vel.x + 2
            self.image = playerRightImage # set the image to looking right
        if (self.rect.x < 0): # if the player is past the left side of the screen, set the pos to the left side of the screen
            self.rect.x = 0
        if (self.rect.x > 750): # if the player in the tornado, move the players pos to outside the tornado.
            self.rect.x = 750

    def PlayerJump(self):
        self.vel.y = -13 # set the y velocity to -13

    def PlayerFly(self):
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

    # Check Functions
    def IsGrounded(self):
        # if the bototm of the palyer is within a small range just above and bellow the ground, than they player is considered grounded
        if (self.rect.bottom < self.screenHeight - self.groundHeight  + 5 and self.rect.bottom > self.screenHeight - self.groundHeight - 5):
            return True
        else: # if not within that range, the player is not grounded
            return False
