import pygame
import os
import Eric_Dumb_Module as edm

# Setup Images
gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')
playerImage = pygame.image.load(os.path.join(imgFolder, 'Player.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, GROUNDHEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImage
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = HEIGHT - 100

        # Player Variables
        self.gravity = 1
        self.vel = edm.Vector(10, 0)

        self.screenHeight = HEIGHT
        self.screenWidth = WIDTH
        self.groundHeight = GROUNDHEIGHT

        self.health = 100
        self.debrisDamage = 34
        self.regenTimer = 0
        self.hasHelmet = False

        self.hasRocketBoots = False
        self.hasFuelcell = False
        self.hasFuelRegen = False
        self.fuel = 10
        self.fuelLimit = 100
        self.fuelTimer = 0


    def update(self):
        # Movement
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT]):
            self.rect.x -= self.vel.x - 2
        if (key[pygame.K_RIGHT]):
            self.rect.x += self.vel.x + 2
        if (self.rect.x < 0):
            self.rect.x = 0
        if (self.rect.x > 750):
            self.rect.x = 750

        # Gravity
        self.rect.y += self.vel.y
        if (self.rect.bottom > self.screenHeight - self.groundHeight):
            self.rect.bottom = self.screenHeight - self.groundHeight
            self.vel.y = 0
        else:
            self.vel.y += self.gravity
            self.rect.x += 2

        if (key[pygame.K_SPACE] and self.fuel > 0):
            self.Rocket()
        if (self.rect.y <= 0 ):
            self.rect.y = 0
            self.vel.y = 1

        # Health and Fuel
        if (self.rect.x > 600):
            self.DrainHP()
        else:
            self.RegenHP()

        self.RegenFuel()

        # Cheats
        if (key[pygame.K_w]):
            self.fuelLimit = 999
            self.fuel = 999
        if (key[pygame.K_e]):
            self.debrisDamage = 0

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
