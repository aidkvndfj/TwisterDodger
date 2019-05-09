import pygame
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

# Colors
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, HEIGHT, WIDTH):
        playerImage = pygame.image.load(os.path.join(imgFolder, 'Player.png'))

        pygame.sprite.Sprite.__init__(self)
        # Player image Setup
        self.image = playerImage
        # self.image = pygame.Surface((20, 60)) # Make the food slightly smaller than the head/tail
        # self.image.fill(WHITE) # Make the food white
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = 200 # Set the x to given x
        self.rect.centery = HEIGHT - 100 # Set the y to given y
        # Player Variables
        self.gravity = 1
        self.xVel = 10
        self.yVel = 0
        self.screenHeight = HEIGHT
        self.screenWidth = WIDTH
        self.health = 100
        self.regenTimer = 0

    def update(self):
        if (self.rect.bottom < self.screenHeight):
            self.yVel += self.gravity
        if (self.rect.bottom > self.screenHeight):
            self.rect.bottom = self.screenHeight
            self.yVel = 0
        self.rect.centery += self.yVel
        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT]):
            self.rect.centerx += -self.xVel + 2
        if (key[pygame.K_RIGHT]):
            self.rect.centerx += self.xVel - 2
        if (self.rect.left < 0):
            self.rect.left = 0
        if (self.rect.right > self.screenWidth - 200):
            self.rect.right = self.screenWidth - 200

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
