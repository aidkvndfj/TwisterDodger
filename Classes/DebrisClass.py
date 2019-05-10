import pygame
import random
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

# Colors
RED = (255, 0, 0)

class Debris(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        # Get Debris Image
        pic = random.randint(1, 3)
        if (pic == 1):
            debrisImage = pygame.image.load(os.path.join(imgFolder, 'Stone1.png'))
        if (pic == 2):
            debrisImage = pygame.image.load(os.path.join(imgFolder, 'Stone2.png'))
        if (pic == 3):
            debrisImage = pygame.image.load(os.path.join(imgFolder, 'Stone3.png'))

        self.image = debrisImage # Set image to the debris image
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
