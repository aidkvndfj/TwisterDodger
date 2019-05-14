import pygame
import random
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

fuelcellImage = pygame.image.load(os.path.join(imgFolder, 'Fuelcell.png'))
helmetImage = pygame.image.load(os.path.join(imgFolder, 'Golden Hard Hat.png'))

class Fuelcell(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = fuelcellImage # Set image to the debris image
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Fuelcell Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight):
            self.kill()

        self.yVel += self.gravity
        self.rect.centerx += self.xVel
        self.rect.centery += self.yVel

    def Collected(self):
        self.kill()
        return "Fuelcell"

class Helmet(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = helmetImage # Set image to the debris image
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Debris Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight):
            self.kill()

        self.yVel += self.gravity
        self.rect.centerx += self.xVel
        self.rect.centery += self.yVel

    def Collected(self):
        self.kill()
        return "Helmet"
