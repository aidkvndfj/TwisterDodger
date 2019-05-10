import easygui as gui
import Game
import time

gui.msgbox("Welcome to Twister Dodger", "Twister Dodger", "Play")
print("\n\n\tYour Time Was: {0:0.2f}s\n\n".format(Game.Game()))
