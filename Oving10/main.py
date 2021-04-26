from Game_v5 import Game
from Gui import Gui

game = Game()

game.random_ship(2,1)
game.random_ship(3,2)
game.random_ship(5,1)
game.random_ship(4,1)

gui = Gui(game)