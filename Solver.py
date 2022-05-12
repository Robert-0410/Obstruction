# Implements minimax with a depth limited search and minimax alpha-beta pruning
import copy
from Board import State
from Tester import Player


# TODO implement a Node class to be used in the Game tree

# TODO implement minimax with depth limited search
class Minimax:
    depth = 1

    def __init__(self, state: State, player: Player):
        self.root = copy.deepcopy(state)  # prevents actual game state from being altered
        self.player = player
        self.game_tree = self.fill_game_tree()  # need method to fill the game tree
        # the algo can build the tree with the necessary values to make the decisions

    def fill_game_tree(self):
        # TODO need method to do a soft move to fill necessary values such as heuristics
        return []  # TODO temp return, needs the game tree as a list

# TODO implement minimax with alpha-beta pruning


# TODO need to make a heuristic function to determine utility value could take in the State
