import copy


class Node:
    def __init__(self, state, parent, blank, cost):
        self.state = state
        self.parent = parent
        self.blank = blank
        self.cost = cost

        # attributes to use in greedy and A* search as heuristic
        self.misplaced = 0
        self.manhattan = 0

    # ===============================================================================================
    #   SUCCESSOR FUNCTION FOR GENERATING REACHABLE NODES FROM A CURRENT NODE
    # ===============================================================================================
    def generate_children(self):
        children = []

        # check if move **UP** is valid then perform the move
        if self.blank[0] - 1 >= 0:
            temp = copy.deepcopy(self.state)
            # substitution the blank with up value
            holder = temp[self.blank[0] - 1][self.blank[1]]
            temp[self.blank[0] - 1][self.blank[1]] = "_"
            temp[self.blank[0]][self.blank[1]] = holder
            # appending child to all children
            new_blank = (self.blank[0] - 1, self.blank[1])
            children.append(Node(temp, self, new_blank, self.cost + 1))

        # check if move **DOWN** is valid then perform move
        if self.blank[0] + 1 <= 2:
            temp = copy.deepcopy(self.state)
            # substitution the blank with up value
            holder = temp[self.blank[0] + 1][self.blank[1]]
            temp[self.blank[0] + 1][self.blank[1]] = "_"
            temp[self.blank[0]][self.blank[1]] = holder
            # appending child to all children
            new_blank = (self.blank[0] + 1, self.blank[1])
            children.append(Node(temp, self, new_blank, self.cost + 1))

        # check if move **LEFT** is valid then perform move
        if self.blank[1] - 1 >= 0:
            temp = copy.deepcopy(self.state)
            # substitution the blank with up value
            holder = temp[self.blank[0]][self.blank[1] - 1]
            temp[self.blank[0]][self.blank[1] - 1] = "_"
            temp[self.blank[0]][self.blank[1]] = holder
            # appending child to all children
            new_blank = (self.blank[0], self.blank[1] - 1)
            children.append(Node(temp, self, new_blank, self.cost + 1))

        # check if move *8RIGHT** is valid then perform move
        if self.blank[1] + 1 <= 2:
            temp = copy.deepcopy(self.state)
            # substitution the blank with up value
            holder = temp[self.blank[0]][self.blank[1] + 1]
            temp[self.blank[0]][self.blank[1] + 1] = "_"
            temp[self.blank[0]][self.blank[1]] = holder
            # appending child to all children
            new_blank = (self.blank[0], self.blank[1] + 1)
            children.append(Node(temp, self, new_blank, self.cost + 1))

        return children

    # ==============================================================================================
    # HEURISTICS TO USE IN A* AND GREEDY BFS ALGORITHMS
    # ==============================================================================================
    # AN ADMISSIBLE HEURISTIC
    def misplaced_tiles(self, goal_state):
        counter = 0
        if self.state[0][0] != goal_state[0][0]: counter += 1
        if self.state[0][1] != goal_state[0][1]: counter += 1
        if self.state[0][2] != goal_state[0][2]: counter += 1
        if self.state[1][0] != goal_state[1][0]: counter += 1
        if self.state[1][1] != goal_state[1][1]: counter += 1
        if self.state[1][2] != goal_state[1][2]: counter += 1
        if self.state[2][0] != goal_state[2][0]: counter += 1
        if self.state[2][1] != goal_state[2][1]: counter += 1
        if self.state[2][2] != goal_state[2][2]: counter += 1
        self.misplaced = counter

    # AN ADMISSIBLE HEURISTIC
    def manhattan_distance(self, goal_state):
        counter = 0
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                value = self.state[i][j]
                counter += abs(i - Node.getRow(value, goal_state)) + \
                           abs(j - Node.getCol(value, goal_state))
        return counter

    # STATIC METHODS FOR COMPARISON BETWEEN TWO NODES
    @staticmethod
    def get_misplaced(node):
        return node.misplaced

    @staticmethod
    def get_misplaced_cost(node):
        return node.misplaced + node.cost

    @staticmethod
    # when it's hard to get an answer, use this
    # it will solve the 8puzzle but not in an optimal way
    def get_misplaced_cost_not_complete(node):
        return node.misplaced * 100 + node.cost

    @staticmethod
    def get_manhattan(node):
        return node.manhattan

    @staticmethod
    def get_manhattan_cost(node):
        return node.manhattan + node.cost

    # ============================================================================================
    #   STATIC METHODS FOR SIMPLE OPERATIONS IN NODE
    # ============================================================================================
    @staticmethod
    # GETTING ROW NUMBER OF A VALUE IN A GIVEN STATE
    def getRow(value, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if value == state[i][j]:
                    return i

    @staticmethod
    # GETTING COL NUMBER OF A VALUE IN A GIVEN STATE
    def getCol(value, state):
        for i in range(len(state)):
            for j in range(len(state)):
                if value == state[i][j]:
                    return j

    @staticmethod
    # GIVING BACK TO COORDINATES OF A BLANK SPACE IN GIVEN STATE
    def find_blank(state):
        for x in range(0, len(state)):
            for y in range(0, len(state[x])):
                if state[x][y] == "_":
                    return x, y

    # =========================================================================================
    #   DEFAULT FUNCTIONS FOR EASE OF COMPARISON AND STRING REPRESENTATION
    # =========================================================================================
    def __str__(self):
        return f"Node With State of {self.state} and Blank at position {self.blank}"

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.state == other.state:
                return True
        return False

    def __gt__(self, other):
        return self.cost >= other.cost
