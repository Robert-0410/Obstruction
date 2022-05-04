# Connects Board and Solver to run Obstruction

# TODO start here by taking command line arguments and set up the move sequence with single action AI outputting "Moved"
import sys

import console as console

# Represents the participants playing against each other (Human, AI)
from Board import start_game_state


# Represents the participants of the game Obstruction
class Player:
    def __init__(self, player: int, is_ai: bool):
        self.player = player
        self.player_id = assign_player_id(player)
        self.is_ai = is_ai


# TODO class: Game, represents entire game and any state that will be coupled
class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.current_board_state = start_game_state()
        self.is_game_over = False


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


# Conducts player move depending on if human or AI
def conduct_move(game: Game, player: Player):
    # human move
    if not player.is_ai:
        print("call function to conduct human move")
        return False
    else:
        print("call function to conduct AI move")
        return True
    # TODO needs to return if move ends game


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
            player1 = Player(1, True)
            player2 = Player(2, False)
        else:
            player1 = Player(1, False)
            player2 = Player(2, True)

            game = Game(player1, player2)
            # TODO continue here getting to the point of proper move sequencing between players
            while not game.is_game_over:
                print("Entered while loop, line 86")
                # ask for move, move method should return if player had a successful move to know if game should be
                # terminated move should update game.is_game_over
                game.is_game_over = conduct_move(game, player1)
                game.is_game_over = conduct_move(game, player2)


# TODO if debug tool is needed call debug_mode() -> need to write still
run()
