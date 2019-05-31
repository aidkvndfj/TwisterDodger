import pygame
import sys
import os

sys.path.insert(0, './Dependencies')
import PyButton
import Game

gameFolder = os.path.dirname("..")
imgFolder = os.path.join(gameFolder, 'Images')

# Initalize
pygame.init()
pygame.font.init()

# Constants
WIDTH = 700 # Standard Width
HEIGHT = 500 # Standard Height
FPS = 30 # Standard FPS

# Colors
BLACK      = (0, 0, 0)
WHITE      = (255, 255, 255)
BACKGROUND = (0, 50, 255)
BUTTONBACK = (40, 40, 40)
BUTTONFONT = (255, 255, 255)

# Other Variables
showInstructions = False
showLeaderboards = False

topScore = 0
secondScore = 0
thirdScore = 0

# Images
titleScreenText = pygame.image.load(os.path.join(imgFolder, 'TitleText.png'))

# Font/Text Setup
leaderboardFont = pygame.font.SysFont(None, 50)
topScoreText = leaderboardFont.render("None: {}".format(topScore), True, WHITE)
secondScoreText = leaderboardFont.render("None: {}".format(secondScore), True, WHITE)
thirdScoreText = leaderboardFont.render("None: {}".format(thirdScore), True, WHITE)

textFont = pygame.font.SysFont(None, 25)
gameWorkText = textFont.render("How The Game Works:", True, WHITE)
controlsText = textFont.render("Controls:", True, WHITE)
arrowText = textFont.render("Use the left and right arrow keys to move the character left and right, you can also", True, WHITE)
arrowText2 = textFont.render("use the space bar to jump.", True, WHITE)
powerupText = textFont.render("Powerups:", True, WHITE)
helmetText = textFont.render("Helmet: A golden helmet will spawn which decreases damage to 25, meaning that it", True, WHITE)
helmetText2 = textFont.render("takes 4 hits from full health to die.", True, WHITE)
rocketbootText = textFont.render("Rocketboots: There will be rocketboots that can spawn which will allow you to", True, WHITE)
rocketbootText2 = textFont.render("fly by holding the space bar.", True, WHITE)
bigFuelCellText = textFont.render("Big Fuel Cell: After collecting the rocketboot, there will be a larger fuel", True, WHITE)
bigFuelCellText2 = textFont.render("cell which will allow you to fly for longer periods.", True, WHITE)
fuelRegenText = textFont.render("Fuel Regenerator: After collecting the rocketboots, there will be a red fuel", True, WHITE)
fuelRegenText2 = textFont.render("regenerator which will allow you to regenerate fuel.", True, WHITE)
fastFuelRegenText = textFont.render("Fast Fuel Regenerator: After collecting the normal fuel regenerator, there", True, WHITE)
fastFuelRegenText2 = textFont.render("will be a green fuel regenerator which will allow you to regenerator fuel", True, WHITE)
fastFuelRegenText3 = textFont.render("after a shorter period, and faster.", True, WHITE)


# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Setup the screen
pygame.display.set_caption("Twister Dodger Menu") # Name the window

# Clock Setup
clock = pygame.time.Clock()

# Sprites/Sprite Groups
menuButtonSprites = pygame.sprite.Group()
otherButtonSprites = pygame.sprite.Group()

playButton = PyButton.PyButton((150, 370, 100, 60), BUTTONBACK, "Play", 50, BUTTONFONT)
exitButton = PyButton.PyButton((550, 370, 100, 60), BUTTONBACK, "Exit", 50, BUTTONFONT)
instructionButton = PyButton.PyButton((350, 370, 225, 60), BUTTONBACK, "Instructions", 50, BUTTONFONT)
leaderboardButton = PyButton.PyButton((350, 450, 500, 60), BUTTONBACK, "Leaderboards", 50, BUTTONFONT)
menuButtonSprites.add(playButton, exitButton, instructionButton, leaderboardButton)

otherExitButton = PyButton.PyButton((640, 460, 100, 60), BUTTONBACK, "Back", 50, BUTTONFONT)
otherButtonSprites.add(otherExitButton)

# Functions
def WriteInstructions():
    # screen.blit(gameWorkText, (10, 10)) # Display the Instruction text onto the screen
    screen.blit(controlsText, (10, 50)) # Display the Instruction text onto the screen
    screen.blit(arrowText, (10, 70)) # Display the Instruction text onto the screen
    screen.blit(arrowText2, (10, 90)) # Display the Instruction text onto the screen
    screen.blit(powerupText, (10, 130)) # Display the Instruction text onto the screen
    screen.blit(helmetText, (10, 150)) # Display the Instruction text onto the screen
    screen.blit(helmetText2, (10, 170)) # Display the Instruction text onto the screen
    screen.blit(rocketbootText, (10, 195)) # Display the Instruction text onto the screen
    screen.blit(rocketbootText2, (10, 215)) # Display the Instruction text onto the screen
    screen.blit(bigFuelCellText, (10, 240)) # Display the Instruction text onto the screen
    screen.blit(bigFuelCellText2, (10, 260)) # Display the Instruction text onto the screen
    screen.blit(fuelRegenText, (10, 285)) # Display the Instruction text onto the screen
    screen.blit(fuelRegenText2, (10, 305)) # Display the Instruction text onto the screen
    screen.blit(fastFuelRegenText, (10, 330)) # Display the Instruction text onto the screen
    screen.blit(fastFuelRegenText2, (10, 350)) # Display the Instruction text onto the screen
    screen.blit(fastFuelRegenText3, (10, 370)) # Display the Instruction text onto the screen

def WriteLeaderboards():
    screen.blit(topScoreText, (300, 200))
    screen.blit(secondScoreText, (300, 250))
    screen.blit(thirdScoreText, (300, 300))

running = True
while(running):
    # Remove everything on the screen
    screen.fill(BACKGROUND)

    # Set the FPS
    clock.tick(FPS)

    # If 'x' in cornner is pressed exit, if 'p' key pressed exti
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            key = pygame.key.get_pressed()
            if (key[pygame.K_p]):
                running = False

    # Update
    menuButtonSprites.update()
    otherButtonSprites.update()

    if (instructionButton.IsPressed() == True):
        showInstructions = True
    if (leaderboardButton.IsPressed() == True):
        showLeaderboards = True
    if (otherExitButton.IsPressed() == True):
        showInstructions = False
        showLeaderboards = False
    if (playButton.IsPressed() == True):
        Game.Game()
    if (exitButton.IsPressed() == True):
        running = False

    # Draw
    if (showInstructions == True):
        WriteInstructions()
        PyButton.DrawButtonTexts(otherButtonSprites, screen)
    elif (showLeaderboards == True):
        WriteLeaderboards()
        PyButton.DrawButtonTexts(otherButtonSprites, screen)
    elif (showInstructions == False):
        screen.blit(titleScreenText, (60, 20))
        menuButtonSprites.draw(screen)
        PyButton.DrawButtonTexts(menuButtonSprites, screen)


    # Display New Frame
    pygame.display.flip()

pygame.quit()
pygame.font.quit()
