from BFS import *
from DFS import *
from UCS import *
from IDS import *
from GREEDY import *
from AH1 import *
from AH2 import *
from AH3 import *
from utility import *
from Game import Game
import sys

# easy
init1 = [['1', '3', '4'], ['8', '6', '2'], ['7', '_', '5']]
# medium
init2 = [['2', '8', '1'], ['_', '4', '3'], ['7', '6', '5']]
# hard
init3 = [['2', '8', '1'], ['4', '6', '3'], ['_', '7', '5']]
# harder
init4 = [['8', '3', '5'], ['4', '1', '6'], ['2', '7', '_']]
# worst
init5 = [['5', '6', '7'], ['4', '_', '8'], ['3', '2', '1']]

goal = [['1', '2', '3'], ['8', '_', '4'], ['7', '6', '5']]

# UNCOMMENT FOR GETTING INPUT FROM THE USER
# user_init, user_goal = get_input()

# creating the game
# first argument is initial state, and second is goal state
game = Game(init2, goal)

# exit the program is game is not solvable
if not is_reachable(game.init.state, game.goal_state):
    unreachable_statement()
    sys.exit()


# ===========================================================================================
#   PERFORMING SEARCH ALGORITHMS
# ===========================================================================================
def run_algorithms():
    print("Starting BFS Algorithm")
    game.goal, game.created_nodes['bfs'] = bfs(game.init, game.goal_state)
    game.calculate_path_cost('bfs')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting DFS Algorithm")
    game.goal, game.created_nodes['dfs'] = dfs(game.init, game.goal_state)
    game.calculate_path_cost('dfs')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting Uniform Cost Search Algorithm")
    game.goal, game.created_nodes['ucs'] = ucs(game.init, game.goal_state)
    game.calculate_path_cost('ucs')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting Iterative Depening Search Algorithm")
    game.goal, game.created_nodes['ids'] = ids(game.init, game.goal_state)
    game.calculate_path_cost('ids')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting Greedy Best Fist Search Algorithm")
    game.goal, game.created_nodes['greedy'] = greedy(game.init, game.goal_state)
    game.calculate_path_cost('greedy')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting A* with misplaced tiles heuristic Algorithm")
    game.goal, game.created_nodes['ah1'] = ah1(game.init, game.goal_state)
    game.calculate_path_cost('ah1')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting A* with manhattan distance heuristic Algorithm")
    game.goal, game.created_nodes['ah2'] = ah2(game.init, game.goal_state)
    game.calculate_path_cost('ah2')
    print('\033[92m____________________________________________ DONE ______________\033[0m')

    print("Starting A* with misplaced tiles * 100 heuristic Algorithm")
    game.goal, game.created_nodes['ah3'] = ah3(game.init, game.goal_state)
    game.calculate_path_cost('ah3')
    print('\033[92m____________________________________________ DONE ______________\033[0m')


run_algorithms()

# ===========================================================================================
# PRINTING THE INFORMATION
# ===========================================================================================
line_seperator()
print("\033[93mPLEASE NOTE THAT AH3 ALGORITHM IS NOT GUARANTEED TO FIND OPTIMAL SOLUTION\033[0m")
line_seperator()
game.print_created_nodes()
line_seperator()
game.print_cost()
line_seperator()
game.print_path()
