import pygame
import os

# Setup Images
gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')
fireImage = pygame.image.load(os.path.join(imgFolder, 'Fire.png'))

class Fire(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, GROUNDHEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = fireImage
        self.rect = self.image.get_rect()

        self.screenWidth = WIDTH
        self.groundHeight = GROUNDHEIGHT
        self.screenHeight = HEIGHT

    def updateFire(self, playerx, playery, playerWidth, playerHeight):
        if (playery + playerHeight > self.screenHeight  - self.groundHeight - 10):
            self.rect.x = self.screenWidth + 35
        else:
            self.rect.y = playery + playerHeight
            self.rect.centerx = playerx + playerWidth / 2
