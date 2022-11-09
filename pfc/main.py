from game import Game
from player import Player

player_1 = Player()
player_2 = Player()
game_class = Game(player_1, player_2)
game_class.play()