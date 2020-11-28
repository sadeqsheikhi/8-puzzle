import bisect


def ucs(init, goal_state):
    frontier, explored, counter = [init], [], 0

    while True:
        # checking for empty frontier
        if len(frontier) == 0:
            return False

        # getting element out of frontier
        temp = frontier.pop(0)
        if temp.state == goal_state:
            return temp, counter
        explored.append(temp)

        # adding valid children to the frontier
        for node in temp.generate_children():
            if node in frontier or node in explored:
                continue
            bisect.insort(frontier, node)

        # printing info and setting the limitation
        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')

        if counter > 10000:
            return "NO Answer In Proper Time", 10000