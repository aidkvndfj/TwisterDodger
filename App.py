import easygui as gui
import Game
import time

scores = open("Scores.txt", "a+")

while (True):

    choice = gui.buttonbox("Welcome to Twister Dodger\n\nPress the space bar to fly, and use left and right arrow keys to move\n\nThere are 2 powerups, a goldenhelmet which reduces damage taken\nand a fuel tank with increase the amount of fuel you can hold.", "Twister Dodger", ("Play", "Leaderboard", "Close"))
    if (choice == "Play"):
        time = Game.Game()
        name = gui.enterbox("Your Time Was: {0:0.2f} seconds\nPlease Input Your Name:".format(time))
        while (name == ""):
            name = gui.enterbox("You Forgot Your Name\n\nYour Time Was: {0:0.2f} seconds\nPlease Input Your Name:".format(time))
        if (name != None):
            scores.write("\n{0}\t{1:0.2f}s".format(name, time))

    if (choice == "Close"):
        break

    if (choice == "Leaderboard"):
        name = gui.msgbox("#1 Djordje: 321s\n#2 Aidan: 279s\n #3 Gurveer 212s", "Leaderboard", "Back")

    choice = ""
