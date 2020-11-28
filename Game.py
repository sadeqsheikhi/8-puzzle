from Node import Node


class Game:
    def __init__(self, init_state, goal_state):
        self.init = Node(init_state, None, Node.find_blank(init_state), 0)
        self.goal_state = goal_state
        self.goal = None

        # holding values of expanded nodes in each algo
        self.created_nodes = {
            "bfs": 0,
            'ucs': 0,
            'dfs': 0,
            'ids': 0,
            'greedy': 0,
            'ah1': 0,
            'ah2': 0,
            'ah3': 0,
        }

        # holding the cost of the solution for each algo
        self.cost = {
            "bfs": 0,
            'ucs': 0,
            'dfs': 0,
            'ids': 0,
            'greedy': 0,
            'ah1': 0,
            'ah2': 0,
            'ah3': 0
        }

        # holding the path in a sequence string ( 1=up 2=down 3=left 4=right )
        self.path = {
            "bfs": '',
            'ucs': '',
            'dfs': '',
            'ids': '',
            'greedy': '',
            'ah1': '',
            'ah2': '',
            'ah3': ''
        }

        # full path in case you want to show the full path
        # not used in current implementation, but feel free to use it
        self.full_path = {
            "bfs": [],
            'ucs': [],
            'dfs': [],
            'ids': [],
            'greedy': [],
            'ah1': [],
            'ah2': [],
            'ah3': []
        }

    # ===========================================================================================
    #  CREATING PATH AND FULL PATH AFTER THE SOLUTION IS GIVEN TO GAME
    # ===========================================================================================
    def calculate_path_cost(self, algo):
        current = self.goal

        if not isinstance(self.goal, Node):
            self.cost[algo] = 'too long'
            self.path[algo] = 'too long'
            return

        # storing full_path
        full_path = [current.state]
        moves = [current.blank]

        # Tracing the parent tree till we reach initial node (bottom to initial)
        while isinstance(current.parent, Node):
            full_path.append(current.parent.state)
            moves.append(current.parent.blank)
            current = current.parent

        # Cost of each step is the same and is 1 (first node has cost 0)
        self.cost[algo] = len(full_path) - 1

        # Getting full path from start to bottom
        full_path.reverse()
        self.full_path[algo] = full_path

        # Calculating Path String Sequence for moves
        moves.reverse()
        for x in range(len(moves) - 1):
            # up
            if moves[x][0] > moves[x + 1][0]:
                self.path[algo] += '1'
            # down
            elif moves[x][0] < moves[x + 1][0]:
                self.path[algo] += '2'
            # left
            elif moves[x][1] > moves[x + 1][1]:
                self.path[algo] += '3'
            # right
            elif moves[x][1] < moves[x + 1][1]:
                self.path[algo] += '4'

    # ===========================================================================================
    # PRINTING USEFUL INFORMATION IN THE CONSOLE
    # ===========================================================================================
    def print_cost(self):
        print("cost of solving is:")
        for key, value in self.cost.items():
            print(f"{key} : {value}")

    def print_path(self):
        print("path to solve is:")
        for key, value in self.path.items():
            print(f"{key} : {value}")

    def print_created_nodes(self):
        print("created nodes to solve are:")
        for key, value in self.created_nodes.items():
            print(f"{key} : {value}")

    # ===========================================================================================
    # STATIC METHODS
    # ===========================================================================================
    @staticmethod
    # DRAWS A STATE ON THE CONSOLE
    # this method is not used in the program, if you want to print the solution you can use this
    def draw_state(state):
        print("_________________________")
        print(f"|\t{state[0][0]} \t|\t{state[0][1]} \t|\t{state[0][2]} \t|")
        print(f"|\t{state[1][0]} \t|\t{state[1][1]} \t|\t{state[1][2]} \t|")
        print(f"|\t{state[1][0]} \t|\t{state[1][1]} \t|\t{state[1][2]} \t|")
        print("-------------------------")
