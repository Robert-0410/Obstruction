# Models the game board and pieces that compose it

# Representation of the actual game state for the game of obstruction.
class State:
    def __init__(self):
        self.state = start_game_state()
        self.adjacent = get_adjacent_mapping()
        self.available_indexes = set_initial_indexes()
        self.mapping_to_index = get_mapping_to_index()

    def place_symbol_and_update_state(self, location, symbol):
        # play
        x = self.mapping_to_index[location]
        index = x.pop()
        s = list(self.state)
        s[index] = symbol
        self.available_indexes.remove(index)
        for i in self.adjacent[index]:
            if i in self.available_indexes:
                s[i] = '/'
                self.available_indexes.remove(i)
        output = ''
        for i in s:
            output += i
        self.state = output

    def display_current_state(self):
        index = 0
        for i in range(6):
            for j in range(6):
                print(self.state[index], end=' ')
                index += 1
            print()


# return the initial game state of the game
def start_game_state():
    return '------------------------------------'


# fill set with the indexes for the board state
def set_initial_indexes():
    output = set()
    for i in range(36):
        output.add(i)
    return output


# Mapping needed to place symbol in correct position
def get_mapping_to_index():
    # row 0 - 5
    # col 0 - 5
    output = {
        '00': {0},
        '01': {1},
        '02': {2},
        '03': {3},
        '04': {4},
        '05': {5},
        '10': {6},
        '11': {7},
        '12': {8},
        '13': {9},
        '14': {10},
        '15': {11},
        '20': {12},
        '21': {13},
        '22': {14},
        '23': {15},
        '24': {16},
        '25': {17},
        '30': {18},
        '31': {19},
        '32': {20},
        '33': {21},
        '34': {22},
        '35': {23},
        '40': {24},
        '41': {25},
        '42': {26},
        '43': {27},
        '44': {28},
        '45': {29},
        '50': {30},
        '51': {31},
        '52': {32},
        '53': {33},
        '54': {34},
        '55': {35}
    }
    return output


# Mapping needed to remove adjacent spaces out of play after a move
def get_adjacent_mapping():
    # 0  1  2  3  4  5
    # 6  7  8  9  10 11
    # 12 13 14 15 16 17
    # 18 19 20 21 22 23
    # 24 25 26 27 28 29
    # 30 31 32 33 34 35
    output = {
        0: {1, 6, 7},
        1: {0, 2, 6, 7, 8},
        2: {1, 3, 7, 8, 9},
        3: {2, 4, 8, 9, 10},
        4: {3, 5, 9, 10, 11},
        5: {4, 10, 11},
        6: {0, 1, 7, 12, 13},
        7: {0, 1, 2, 6, 8, 12, 13, 14},
        8: {1, 2, 3, 7, 9, 13, 14, 15},
        9: {2, 3, 4, 8, 10, 14, 15, 16},
        10: {3, 4, 5, 9, 11, 15, 16, 17},
        11: {4, 5, 10, 16, 17},
        12: {6, 7, 13, 18, 19},
        13: {6, 7, 8, 12, 14, 18, 19, 20},
        14: {7, 8, 9, 13, 15, 19, 20, 21},
        15: {8, 9, 10, 14, 16, 20, 21, 22},
        16: {9, 10, 11, 15, 17, 21, 22, 23},
        17: {10, 11, 16, 22, 23},
        # 0  1  2  3  4  5
        # 6  7  8  9  10 11
        # 12 13 14 15 16 17
        # 18 19 20 21 22 23
        # 24 25 26 27 28 29
        # 30 31 32 33 34 35
        18: {12, 13, 19, 24, 25},
        19: {12, 13, 14, 18, 20, 24, 25, 26},
        20: {13, 14, 15, 19, 21, 25, 26, 27},
        21: {14, 15, 16, 20, 22, 26, 27, 28},
        22: {15, 16, 17, 21, 23, 27, 28, 29},
        23: {16, 17, 22, 28, 29},
        24: {18, 19, 25, 30, 31},
        25: {18, 19, 20, 24, 26, 30, 31, 32},
        26: {19, 20, 21, 25, 27, 31, 32, 33},
        27: {20, 21, 22, 26, 28, 32, 33, 34},
        28: {21, 22, 23, 27, 29, 33, 34, 35},
        29: {22, 23, 28, 34, 35},
        30: {24, 25, 31},
        31: {24, 25, 26, 30, 32},
        32: {25, 26, 27, 31, 33},
        33: {26, 27, 28, 32, 34},
        34: {27, 28, 29, 33, 25},
        35: {28, 29, 34}
    }
    return output

# TODO class: GameState not sure if I need too
# TODO class: Snapshot, snapshot of what the game will look like with specific move
# TODO class: Tile, individual positions that make up the board game

#  game = State()
#  game.display_current_state()
#  game.place_symbol_and_update_state('00', 'X')
#  print("placed symbol")
#  game.display_current_state()
#  print("Number of available places: ", len(game.available_indexes))
#  print(game.available_indexes)
#  game.place_symbol_and_update_state('02', 'O')
#  print("placed symbol")
#  game.display_current_state()
#  print("Number of available places: ", len(game.available_indexes))
#  print(game.available_indexes)
#  game.place_symbol_and_update_state('21', 'X')
#  print("placed symbol")
#  game.display_current_state()
#  print("Number of available places: ", len(game.available_indexes))
#  print(game.available_indexes)
