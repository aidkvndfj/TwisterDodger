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

    def update(self):
        # Movement
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT]):
    
    def update(self):

    def update(self):
        # Movement
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT]):
        # Movement
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT]):
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT]):
            self.rect.x -= self.vel.x
        if (key[pygame.K_RIGHT]):
            self.rect.x += self.vel.x

        # Gravity
        self.rect.y += self.vel.y
        if (self.rect.bottom > self.screenHeight - self.groundHeight):
            self.rect.bottom = self.screenHeight - self.groundHeight
        else:
            self.vel.y += self.gravity

    def GetHit(self):
        self.health -= 34
        self.regenTimer = 5

    def drainHP(self):
        self.health -= 0.5

    def regenHP(self):
        if (self.health < 100 and self.regenTimer <= 0):
            self.health += 1
        else:
            self.regenTimer -= 0.1

    def Jump(self):
        self.yVel -= 10
