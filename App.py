import easygui as gui
import Game
import time

scores = open("Scores.txt", "a+")

while (True):
    choice = gui.buttonbox("Welcome to Twister Dodger\nArrows Key To Move, Space To Jump", "Twister Dodger", ("Play", "Close"))
    if (choice == "Play"):
        time = Game.Game()
        name = gui.enterbox("Your Time Was: {0:0.2f} seconds\nPlease Input Your Name:".format(time))
        while (name == ""):
            name = gui.enterbox("You Forgot Your Name\n\nYour Time Was: {0:0.2f} seconds\nPlease Input Your Name:".format(time))
        scores.write("\n{0}\t{1:0.2f}s".format(name, time))


    if (choice == "Close"):
        break
    choice = ""
