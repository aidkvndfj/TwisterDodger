import pygame
import random
import os

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

bigFuelcellImage = pygame.image.load(os.path.join(imgFolder, 'BigFuelcell.png'))
helmetImage = pygame.image.load(os.path.join(imgFolder, 'Golden Hard Hat.png'))
rocketbootsImage = pygame.image.load(os.path.join(imgFolder, 'RocketBoots.png'))
fuelRegeneratorImage = pygame.image.load(os.path.join(imgFolder, 'FuelRegenerator.png'))
fastFuelRegeneratorImage = pygame.image.load(os.path.join(imgFolder, 'FastFuelRegenerator.png'))

class Helmet(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = helmetImage # Set image to the helmet image
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Helmet Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight): # if the helmet is bellow the screen
            self.kill() #destory the objects

        self.yVel += self.gravity # add gravity to y vel
        self.rect.centerx += self.xVel # move x pos by x vel
        self.rect.centery += self.yVel # move y pos by y vel

    def Collected(self): # gets called if the player collects the helmet
        self.kill() # kill the object
        return "Helmet" # return the powerup type

class RocketBoots(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = rocketbootsImage
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Rocket Boots Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight): # if the boots are bellow the screen
            self.kill() #destory the objects

        self.yVel += self.gravity # add gravity to y vel
        self.rect.centerx += self.xVel # move x pos by x vel
        self.rect.centery += self.yVel # move y pos by y vel

    def Collected(self): # gets called if the player collects the rocket boots
        self.kill() # kill the object
        return "RocketBoots" # return the powerup type

class BigFuelcell(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = bigFuelcellImage # Set image to the big fuel cell image
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Big Fuelcell Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight): # if the big fuel cell is bellow the screen
            self.kill() #destory the objects

        self.yVel += self.gravity # add gravity to y vel
        self.rect.centerx += self.xVel # move x pos by x vel
        self.rect.centery += self.yVel # move y pos by y vel

    def Collected(self): # gets called if the player collects the big fuel cell
        self.kill() # kill the object
        return "BigFuelcell" # return the powerup type

class FuelRegenerator(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = fuelRegeneratorImage
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Fuel Regenerator Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight): # if the fuel regenerator is bellow the screen
            self.kill() #destory the objects

        self.yVel += self.gravity # add gravity to y vel
        self.rect.centerx += self.xVel # move x pos by x vel
        self.rect.centery += self.yVel # move y pos by y vel

    def Collected(self): # gets called if the player collects the fuel regenerator
        self.kill() # kill the object
        return "FuelRegenerator" # return the powerup type

class FastFuelRegenerator(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)

        self.image = fastFuelRegeneratorImage
        self.rect = self.image.get_rect() #set the rect to the image rect
        self.rect.centerx = WIDTH - 150 # Set the x to given x
        self.rect.centery = random.randint(0, HEIGHT - 200) # Set the y to given y

        # Fast Fuel Regenerator Variables
        self.screenHeight = HEIGHT
        self.gravity = 0.5
        self.xVel = -random.randint(10, 25)
        self.yVel = 0

    def update(self):
        if (self.rect.y > self.screenHeight): # if the fast fuel regenerator is bellow the screen
            self.kill() #destory the objects

        self.yVel += self.gravity # add gravity to y vel
        self.rect.centerx += self.xVel # move x pos by x vel
        self.rect.centery += self.yVel # move y pos by y vel

    def Collected(self): # gets called if the player collects the fast fuel regenerator
        self.kill() # kill the object
        return "FastFuelRegenerator" # return the powerup type
