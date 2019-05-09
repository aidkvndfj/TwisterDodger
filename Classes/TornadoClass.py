import pygame
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

# Colors
RED = (255, 0, 0)

class Tornado(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        tornadoImage = pygame.image.load(os.path.join(imgFolder, 'tornado.png'))

        pygame.sprite.Sprite.__init__(self)
        # Debris image Setup
        self.image = tornadoImage
        # self.image = pygame.Surface((20, 20)) # Make the food slightly smaller than the head/tail
        # self.image.fill(RED) # Make the food white
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.x = WIDTH - 350 # Set the x to given x
        self.rect.y = 0 # Set the y to given y
