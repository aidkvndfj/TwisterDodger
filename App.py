import pygame
import PyButton
import Game

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
RED        = (255, 0, 0)
GREEN      = (0, 255, 0)
BLUE       = (25, 66, 250)

# Font/Text Setup
textFont = pygame.font.SysFont(None, 25)
myText = textFont.render("Text Here", True, WHITE)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Setup the screen
pygame.display.set_caption("Twister Dodger Menu") # Name the window

# Clock Setup
clock = pygame.time.Clock()

# Sprites/Sprite Groups
buttonSprites = pygame.sprite.Group()

playButton = PyButton.PyButton((WIDTH / 2, HEIGHT / 2, 650, 450), WHITE, "Play", 240, BLACK)
buttonSprites.add(playButton)

running = True
while(running):
    # Remove everything on the screen
    screen.fill(BLACK)

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
    buttonSprites.update()
    if (playButton.IsPressed() == True):
        Game.Game()

    # Draw
    buttonSprites.draw(screen)
    PyButton.DrawButtonTexts(buttonSprites, screen)

    # Display New Frame
    pygame.display.flip()

pygame.quit()
pygame.font.quit()


# scores = open("Scores.txt", "a+")
#
# running = True
# while (running):
#     choice = gui.buttonbox("Welcome to Twister Dodger\n\nPress the space bar to fly, and use left and right arrow keys to move\n\nThere are 2 powerups, a goldenhelmet which reduces damage taken\nand a fuel tank with increase the amount of fuel you can hold.", "Twister Dodger", ("Play", "Leaderboard", "Close"))
#     if (choice == "Play"):
#         time = Game.Game()
#         name = gui.enterbox("Your Time Was: {0:0.2f} seconds\nPlease Input Your Name:".format(time))
#         while (name == ""):
#             name = gui.enterbox("You Forgot Your Name\n\nYour Time Was: {0:0.2f} seconds\nPlease Input Your Name:".format(time))
#         if (name != None):
#             scores.write("\n{0}\t{1:0.2f}s".format(name, time))
#
#     if (choice == "Close"):
#         break
#
#     if (choice == "Leaderboard"):
#         name = gui.msgbox("#1 Djordje: 321s\n#2 Aidan: 279s\n #3 Gurveer 212s", "Leaderboard", "Back")
#
#     choice = ""
