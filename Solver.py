# Implements minimax with a depth limited search and minimax alpha-beta pruning
import copy
from Board import State, get_key_to_index

# Foreshadowing depth for the AI player has
depth = 2


# Node class to be used in the Game tree
class Node:

    def __init__(self, state: State, tree_depth: int, parent, move: str):
        self.parent = parent
        self.move = move
        self.node_state = copy.deepcopy(state)
        self.branching_factor = len(self.node_state.available_indexes)
        self.tree_depth = tree_depth
        self.is_leaf = False
        self.utility_value = 0

        if tree_depth >= depth:
            self.is_leaf = True
        else:
            self.tree = self.add_children()
            self.utility_value = self.grab_utility_value_from_children()

        if self.is_leaf and self.parent is not None:
            self.utility_value = set_heuristic_value(self, 1)
        # set the move that the AI would take
        if self.parent is None:
            # from root find out where roots utility value came from and assign that move the move to take
            self.move_to = self.grab_move()

    def add_children(self):
        output = list()
        output.append(self)
        potential_moves = copy.deepcopy(self.node_state.available_indexes)
        current_index = 1
        while len(potential_moves) != 0:
            current = copy.deepcopy(self.node_state)
            # get input to update state
            index = potential_moves.pop()
            move = get_key_to_index(index)
            # make move to update current
            current.place_symbol_and_update_state(move, '/')
            output.append(Node(current, self.tree_depth + 1, self, move))
            current_index += 1
        if len(potential_moves) == 0:
            self.is_leaf = True
        return output

    # TODO: make alpha beta pruning version of this function that removes any repeated nodes with the same utility
    def grab_utility_value_from_children(self):
        output = 0
        for i in self.tree:
            if output < i.utility_value:
                output = i.utility_value
        return output

    def grab_move(self):
        self.tree.pop(0)
        root_util = self.utility_value
        for i in self.tree:
            if root_util == i.utility_value:
                break
        return copy.deepcopy(i.move)


# minimax with depth limited search
class Minimax:

    def __init__(self, state: State, player: int):
        self.root = Node(state, 0, None, None)
        self.player = player
        self.the_move_chosen = self.root.move_to


# TODO make changes for AlphaBeta
class AlphaBetaPruning:

    def __init__(self, state: State, player: int):
        self.root = Node(state, 0, None, None)
        self.player = player
        self.the_move_chosen = self.root.move_to


def set_heuristic_value(node: Node, player):
    flag = node.branching_factor
    if flag == 0:
        # winning case for MAX
        if player == 1:
            return 100
        # winning case for MIN
        else:
            return -100
    # evaluate for max
    if player == 1:
        return node.parent.branching_factor - flag  # TODO temp return
    # evaluate for MIN
    else:
        return -1  # TODO temp return; might be (prior spaces - current)
