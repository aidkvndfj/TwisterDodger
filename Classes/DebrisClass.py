import pygame
import random
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

# Colors
RED = (255, 0, 0)

class Debris(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pic = random.randint(1, 3)
        if (pic == 1):
            debrisImage = pygame.image.load(os.path.join(imgFolder, 'Stone1.png'))
        if (pic == 2):
            debrisImage = pygame.image.load(os.path.join(imgFolder, 'Stone2.png'))
        if (pic == 3):
            debrisImage = pygame.image.load(os.path.join(imgFolder, 'Stone3.png'))

        pygame.sprite.Sprite.__init__(self)
        # Debris image Setup
        self.image = debrisImage
        # self.image = pygame.Surface((20, 20)) # Make the food slightly smaller than the head/tail
        # self.image.fill(RED) # Make the food white
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y
        # Debris Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        self.yVel += self.gravity
        self.rect.centerx += self.xVel
        self.rect.centery += self.yVel
