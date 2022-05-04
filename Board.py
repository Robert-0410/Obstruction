# Models the game board and pieces that compose it

from Tester import Player


# TODO class: Game, represents entire game and any state that will be coupled
class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

# TODO class: GameState not sure if I need too
# TODO class: Snapshot, snapshot of what the game will look like with specific move
# TODO class: Tile, individual positions that make up the board game

