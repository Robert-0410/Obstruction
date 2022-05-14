# Implements minimax with a depth limited search and minimax alpha-beta pruning
import copy
from Board import State, get_key_to_index

# Foreshadowing depth the AI player has
depth = 2


# TODO implement a Node class to be used in the Game tree
class Node:

    def __init__(self, state: State):
        self.node_state = copy.deepcopy(state)
        self.branching_factor = len(self.node_state.available_indexes)
        self.tree = self.add_children()

    def add_children(self):
        output = list()
        output.append(self)
        potential_moves = copy.deepcopy(self.node_state.available_indexes)
        for i in range(self.branching_factor):
            current = copy.deepcopy(self.node_state)
            # get input to update state
            index = potential_moves.pop()
            move = get_key_to_index(index)
            # make move to update current
            current.place_symbol_and_update_state(move, '-')
            current.display_current_state()
            output[i + 1] = Node(current)
        return output


# TODO implement minimax with depth limited search
class Minimax:

    def __init__(self, state: State, player: int):
        self.root = Node(state)
        self.player = player
        #self.game_tree = self.fill_game_tree()  # need method to fill the game tree
        # TODO set an attribute that calls a method returns the correct format to pass to update state in Tester.py

    #def fill_game_tree(self):
    #    return []  # TODO temp return, needs the game tree as a list


# TODO implement minimax with alpha-beta pruning


# TODO might have to take in a Node object instead
def set_heuristic_value(state: State, player):
    num_of_available_spaces = len(state.available_indexes)
    if num_of_available_spaces == 0:
        # winning case for MAX
        if player == 1:
            return 100
        # winning case for MIN
        else:
            return -100
    # evaluate for max
    if player == 1:
        return 1  # TODO temp return
    # evaluate for MIN
    else:
        return -1  # TODO temp return; might be (prior spaces - current)
