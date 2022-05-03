# Connects Board and Solver to run Obstruction

# TODO start here by taking command line arguments and set up the move sequence with single action AI outputting "Moved"
import console as console


# Represents the participants playing against each other (Human, AI)
class Agent:
    def __init__(self, player: int):
        self.player = player
        self.player_id = assign_player_id(player)


# assigns the character that player will use to occupy space on the game board, X is Max and O is Min
def assign_player_id(player: int):
    output = ''
    if player == 1:
        output = 'X'
    elif player == 2:
        output = 'O'
    else:
        console.error("Player ID was not assigned to X or O.")
        return 'err'


agent1 = Agent(1)
agent2 = Agent(2)
agent_err = Agent(0)
