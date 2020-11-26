import re


def line_seperator():
    print("***********************************************")


# Getting init and goal as user input
def get_input():
    # getting initial state
    while True:
        while True:
            init = input(
                "Enter The Initial State of Your 8 puzzle:\n\
In this format 1,2,3,4,5,6,7,8,_: (you can omit commas) \n\t"
            )
            init = init.replace(" ", '').replace(",", "")
            if (re.search(r"^(?:([1-8_])(?!.*\1+)){9}$", init)) is not None:
                print('\033[92m________________________________________correct input______\033[0m')
                break

            print('\033[91m*********** Wrong Input, Try Again Please: **************\033[0m')

        # getting second state
        while True:
            goal = input("Enter The Goal State:\n"
                         "in this format 1,2,3,4,5,6,7,8,_  (you can omit commas)\n\t"
                         )
            goal = goal.replace(" ", "").replace(",", "")
            if re.search(r"^(?:([1-8_])(?!.*\1+)){9}$", goal) is not None:
                print('\033[92m________________________________________correct input______\033[0m')
                break

            print("\033[91m*********** Wrong Input, Try Again Please: *************\033[0m")

        init = make_matrix(init)
        goal = make_matrix(goal)

        validity = is_reachable(init, goal)
        if validity:
            break

        unreachable_statement()
    print("input submitted, now performing algorithms")
    return init, goal


def is_reachable(init, goal):
    permutation_inversion = 0

    init = flatten_matrix(init)
    goal = flatten_matrix(goal)

    # first go through every item in init
    for x in range(len(init)):
        allowed_after = ['_']
        if init[x] == '_':
            continue

        # find out what is allowed to come after it
        counter = 9
        for y in range(len(goal)):
            if init[x] == goal[y]:
                counter = y

            if y > counter:
                allowed_after.append(goal[y])

        # if it's not allowed it's an inversion
        for z in range(x + 1, len(init)):
            if init[z] not in allowed_after:
                permutation_inversion += 1

    if permutation_inversion % 2 == 1:
        return False
    return True


def flatten_matrix(matrix):
    result = []
    for x in matrix:
        for y in x:
            result.append(y)
    return result


def make_matrix(array):
    result = []
    row1, row2, row3 = [], [], []
    for x in range(len(array)):
        if x < 3:
            row1.append(array[x])
        elif x < 6:
            row2.append(array[x])
        elif x < 9:
            row3.append(array[x])
    result.append(row1)
    result.append(row2)
    result.append(row3)
    return result


def unreachable_statement():
    print("\033[93m************************* Warning *************************\033[0m")
    print('The goal state is not reachable from the initial state')
    print('It means that they are disjoint nodes in the state space')
    print('please try again with different initial state and goal')
    print("\033[93m************************* Warning *************************\033[0m")
