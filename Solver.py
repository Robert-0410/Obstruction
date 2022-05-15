# Implements minimax with a depth limited search and minimax alpha-beta pruning
import copy
from Board import State, get_key_to_index

# Foreshadowing depth the AI player has
depth = 2


# TODO implement a Node class to be used in the Game tree
class Node:

    def __init__(self, state: State, tree_depth: int, parent, move: str):
        # TODO: need access to: the move, parent, player
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
            self.tree = self.add_children()  # TODO could assign parents utility after this line
        if self.is_leaf and self.parent is not None:
            self.utility_value = set_heuristic_value(self, 1)  # TODO temp treating as MAX unless I find a better way
        print("Is leaf: ", self.is_leaf)
        print("Node at depth: ", self.tree_depth)
        print("Utility value: ", self.utility_value)
        print("Move is: ", self.move)
        print("Finished a Node()")

    def add_children(self):
        print("Called add_children()")
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
            current.display_current_state()
            output.append(Node(current, self.tree_depth + 1, self, move))
            print("moving to next child")
            current_index += 1
        if len(potential_moves) == 0:
            self.is_leaf = True
        return output


# TODO implement minimax with depth limited search
class Minimax:

    def __init__(self, state: State, player: int):
        self.root = Node(state, 0, None, None)
        self.player = player
        # TODO attribute to access the actual move

# TODO implement minimax with alpha-beta pruning


# TODO might have to take in a Node object instead
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
