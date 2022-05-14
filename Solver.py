# Implements minimax with a depth limited search and minimax alpha-beta pruning
import copy
from Board import State


# TODO implement a Node class to be used in the Game tree

# TODO implement minimax with depth limited search
class Minimax:
    depth = 1

    def __init__(self, state: State):
        self.root = copy.deepcopy(state)  # prevents actual game state from being altered
        # self.player = player #  instead of passing entire Player pass just the values to prevent circular import
        self.game_tree = self.fill_game_tree()  # need method to fill the game tree
        # the algo can build the tree with the necessary values to make the decisions

    def fill_game_tree(self):
        # TODO need method to do a soft move to fill necessary values such as heuristics
        return []  # TODO temp return, needs the game tree as a list

# TODO implement minimax with alpha-beta pruning


# TODO need to make a heuristic function to determine utility value could take in the State
def get_heuristic_value(state: State, player):
    num_of_available_spaces = len(state.available_indexes)
    if num_of_available_spaces == 0:
        # winning case for MAX
        if player == 1:
            return 100
        # winning cas for MIN
        else:
            return -100


