# Connects Board and Solver to run Obstruction

# TODO start here by taking command line arguments and set up the move sequence with single action AI outputting "Moved"
import sys
import console as console
from Board import State, get_mapping_to_index
# from Solver import Minimax


# Represents the participants of the game Obstruction
from Solver import Minimax


class Player:
    def __init__(self, player: int, is_ai: bool):
        self.player_num = player
        self.player_id = assign_player_id(player)
        self.is_ai = is_ai


# represents entire game and any state that will be coupled Player 1: MAX, 2: MIN
class Game:
    def __init__(self, player1: Player, player2: Player, search_method):
        self.player1 = player1
        self.player2 = player2
        self.board_state = State()
        self.is_game_over = False
        self.ai_search_method = search_method


# assigns the character that player will use to occupy space on the game board, X is Max and O is Min
def assign_player_id(player: int):
    if player == 1:
        output = 'X'
    elif player == 2:
        output = 'O'
    else:
        console.error("Player ID was not assigned to X or O.")
        return 'err'
    return output


# Verify human input is correct TODO need to check for letters, currently breaks with input such as lkdfh
def verify_human_input(human_input: list, game: Game):
    if len(human_input) > 2:
        return False

    check = ''
    for i in human_input:
        if int(i) > 5 or int(i) < 0:
            return False
        check += i
    #  x = game.board_state.mapping_to_index[check]
    x = get_mapping_to_index()[check]
    index = x.pop()
    if index not in game.board_state.available_indexes:
        return False
    return True


# Conducts player move depending on if human or AI
def conduct_move(game: Game, player: Player):
    # human move
    if not player.is_ai:
        # Get human player input
        raw_input = input("Input format row/column ex: 3/4: ")
        move_coordinates = raw_input.split('/')
        correct_input = verify_human_input(move_coordinates, game)
        while not correct_input:
            raw_input = input("Input format row/column ex: 3/4: ")
            move_coordinates = raw_input.split('/')
            correct_input = verify_human_input(move_coordinates, game)
        move_location = ''
        for i in move_coordinates:
            move_location += i
        game.board_state.place_symbol_and_update_state(move_location, player.player_id)
        game_over_flag = len(game.board_state.available_indexes)

        if game_over_flag == 0:
            return True
        else:
            return False
    else:
        # TODO call respective algorithm
        print("call function to conduct AI move")
        if game.ai_search_method == 'MM':
            # make algo object
            plan_move = Minimax(game.board_state, player.player_num)
            game.board_state.place_symbol_and_update_state(plan_move.the_move_chosen, player.player_id)
        elif game.ai_search_method == 'AB':
            # TODO call algorithm to conduct ai move
            return False  # temp return
            # make algo object
            # call game.board_state.place_symbol_and_update_state()
        # TODO implement block below once at least one algo is ready for testing
        game_over_flag = len(game.board_state.available_indexes)
        if game_over_flag == 0:
            return True
        else:
            return False


def run():
    if len(sys.argv) == 3:
        if sys.argv[1].isdigit():
            ai_player_id = int(sys.argv[1])
            search_method = sys.argv[2]
        else:
            ai_player_id = None
            search_method = None
            print("Improper command line input")
            exit(0)
    else:
        print("Need arguments or improper format.")
        exit(0)

    if ai_player_id == 1 or ai_player_id == 2 and search_method == "MM" or search_method == 'AB':
        supported = True
    else:
        supported = False

    if not supported:
        print("Arguments currently not supported.")
        exit(0)
    else:
        print("AI Player: ", ai_player_id, ", ", "Search: ", search_method)
        if ai_player_id == 1:
            print("AI is player 1")
            player1 = Player(1, True)
            player2 = Player(2, False)
        else:
            print("AI is player 2")
            player1 = Player(1, False)
            player2 = Player(2, True)

            game = Game(player1, player2, search_method)
            # TODO continue here getting to the point of proper move sequencing between players
            while not game.is_game_over:
                print("Entered while loop, line 90")
                # ask for move, move method should return if player had a successful move to know if game should be
                # terminated move should update game.is_game_over
                game.is_game_over = conduct_move(game, player1)
                game.is_game_over = conduct_move(game, player2)


# TODO if debug tool is needed call debug_mode() -> need to write still
def debug_run():
    search_method = 'MM'
    player1 = Player(1, False)  # False means not AI
    player2 = Player(2, True)

    game = Game(player1, player2, search_method)
    while not game.is_game_over:
        # First player move AKA MAX
        game.board_state.display_current_state()
        game.is_game_over = conduct_move(game, player1)
        game.board_state.display_current_state()

        # Second player move AKA MIN
        game.is_game_over = conduct_move(game, player2)
        game.board_state.display_current_state()


# run()

debug_run()
