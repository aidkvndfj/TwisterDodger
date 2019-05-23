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

        # Player Variables
        self.gravity = 1.5
        self.vel = edm.Vector(10, 0)

        self.screenHeight = HEIGHT
        self.screenWidth = WIDTH
        self.groundHeight = GROUNDHEIGHT

        self.airTimer = 0
        self.playerFlying = False

        self.health = 100
        self.debrisDamage = 34
        self.regenTimer = 0
        self.hasHelmet = False

        self.hasRocketBoots = False
        self.hasFuelcell = False
        self.hasFuelRegen = False
        self.fuel = 100
        self.fuelLimit = 100
        self.fuelTimer = 0

    # Standard update function
    def update(self):
        key = pygame.key.get_pressed()

        print(self.airTimer)

        if (key[pygame.K_SPACE]):
            if (self.IsGrounded()):
                self.PlayerJump()
                self.playerFlying = False
            elif (self.airTimer > 0.5):
                self.PlayerFly()
                self.playerFlying = True

        self.PlayerWalk(key)
        self.PlayerFall()

        # Gravity
        # self.rect.y += self.vel.y
        # if (self.rect.bottom > self.screenHeight - self.groundHeight):
        #     self.rect.bottom = self.screenHeight - self.groundHeight
        #     self.vel.y = 0
        # else:
        #     self.vel.y += self.gravity
        #     self.rect.x += 2
        #
        # if (key[pygame.K_SPACE] and self.fuel > 0):
        #     self.Rocket()
        # if (self.rect.y <= 0 ):
        #     self.rect.y = 0
        #     self.vel.y = 1

        # Health and Fuel
        if (self.rect.x > 600):
            self.DrainHP()
        else:
            self.RegenHP()

        # self.RegenFuel()

        # Cheats
        if (key[pygame.K_w]):
            self.fuelLimit = 999
            self.fuel = 999
        if (key[pygame.K_e]):
            self.debrisDamage = 0

    # Movement functions
    def PlayerWalk(self, key):
        if (key[pygame.K_LEFT]):
            self.rect.x -= self.vel.x - 2
            self.image = playerLeftImage
        if (key[pygame.K_RIGHT]):
            self.rect.x += self.vel.x + 2
            self.image = playerRightImage
        if (self.rect.x < 0):
            self.rect.x = 0
        if (self.rect.x > 750):
            self.rect.x = 750

    def PlayerJump(self):
        self.vel.y = -13

    def PlayerFly(self):
        if (self.fuel > 0):
            self.vel.y -= 2
            self.fuel -= 1
        else:
            self.fuel = 0

    def PlayerFall(self):
        self.rect.y += self.vel.y
        if (self.rect.bottom > self.screenHeight - self.groundHeight):
            self.rect.bottom = self.screenHeight - self.groundHeight
            self.vel.y = 0
        else:
            self.vel.y += self.gravity

        if (self.IsGrounded() == False):
            self.airTimer += 0.1
        else:
            self.airTimer = 0

    # Stat Manipulation Functions
    def GetHit(self):
        self.health -= self.debrisDamage
        self.regenTimer = 5
        if (self.health < 0):
            self.health = -0.1

    def DrainHP(self):
        if (self.health > 0):
            self.health -= 0.5

    def RegenHP(self):
        if (self.health < 100 and self.regenTimer <= 0):
            self.health += 1
        else:
            self.regenTimer -= 0.1

    def Rocket(self):
        self.fuelTimer = 5
        if (self.vel.y > -15):
            self.vel.y -= 2
            self.fuel -= 2
            if (self.fuel < 0):
                self.fuel = 0

    def RegenFuel(self):
        if (self.fuel < self.fuelLimit and self.fuelTimer <= 0):
            self.fuel += 1
        else:
            self.fuelTimer -= 0.1

    def GetHelmet(self):
        self.hasHelmet = True
        self.debrisDamage = 25
        playerImage = pygame.image.load(os.path.join(imgFolder, 'PlayerWithHat.png'))
        self.image = playerImage

    def GetFuelcell(self):
        self.hasFuelcell = True
        self.fuelLimit = 150
        self.fuel = 150

    # Check Functions
    def IsGrounded(self):
        if (self.rect.bottom < self.screenHeight - self.groundHeight  + 5 and self.rect.bottom > self.screenHeight - self.groundHeight - 5):
            return True
        else:
            return False
