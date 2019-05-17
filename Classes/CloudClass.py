import pygame
import random
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

cloudImage = pygame.image.load(os.path.join(imgFolder, 'Cloud.png'))

class Cloud(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = cloudImage # Set image to the debris image
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.left = random.randint(WIDTH, WIDTH + 300) # Set the x to given x
        self.rect.y = random.randint(0, 200) # Set the y to given y

        # Fuelcell Variables
        self.screenHeight = HEIGHT
        self.screenWidth = WIDTH
        self.xVel = -random.randint(2, 5)

    def update(self):
        self.rect.centerx += self.xVel
        if (self.rect.right < 0):
            self.rect.x = random.randint(self.screenWidth, self.screenWidth + 300)
            self.rect.y = random.randint(0, 200)
            self.xVel = -random.randint(2, 5)
