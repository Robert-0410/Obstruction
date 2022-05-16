# Implements minimax with a depth limited search and minimax alpha-beta pruning
import copy
from Board import State, get_key_to_index


depth = 2
nodes_expanded = 0


def get_nodes_expanded():
    global nodes_expanded
    return nodes_expanded


def add_node_count():
    global nodes_expanded
    nodes_expanded += 1


def subtract_node_count():
    global nodes_expanded
    nodes_expanded -= 1


# Node class to be used in the Game tree
class Node:

    def __init__(self, state: State, tree_depth: int, parent, move: str, algo: str):
        self.algo = algo
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
            if algo == 'MM':
                self.utility_value = self.grab_utility_value_from_children()  # TODO logic for diff algos
            elif algo == 'AB':
                self.utility_value = self.grab_utility_from_children_ab()

        if self.is_leaf and self.parent is not None:
            self.utility_value = set_heuristic_value(self, 1)
        # set the move that the AI would take
        if self.parent is None:
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
            output.append(Node(current, self.tree_depth + 1, self, move, self.algo))
            add_node_count()
            current_index += 1
        if len(potential_moves) == 0:
            self.is_leaf = True
        return output

    def grab_utility_value_from_children(self):
        output = 0
        for i in self.tree:
            if output < i.utility_value:
                output = i.utility_value
        return output

    def grab_utility_from_children_ab(self):
        output = 0
        for i in self.tree:
            if output < i.utility_value:
                output = i.utility_value

            if output == i.utility_value:
                self.tree.remove(i)
                subtract_node_count()
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

    def __init__(self, state: State, player: int, algo: str):
        self.root = Node(state, 0, None, None, algo)
        self.player = player
        self.the_move_chosen = self.root.move_to
        self.total_expanded = get_nodes_expanded()


# minimax with AlphaBeta pruning
class AlphaBetaPruning:

    def __init__(self, state: State, player: int, algo: str):
        self.root = Node(state, 0, None, None, algo)
        self.player = player
        self.the_move_chosen = self.root.move_to
        self.total_expanded = get_nodes_expanded()


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
        return node.parent.branching_factor - flag
    # evaluate for MIN
    else:
        return -1
