from Node import Node


def greedy(init, goal_state):
    frontier = [init]
    counter = 0
    while True:
        # checking for empty frontier
        if len(frontier) == 0:
            return False

        # getting element out of frontier
        temp = frontier.pop(0)
        if temp.state == goal_state:
            return temp, counter

        # adding valid children to the frontier
        children = temp.generate_children()
        for node in children:
            if node == temp.parent:
                continue
            # inserting into the frontier in a sorted way based on manhattan_distance heuristic
            node.manhattan_distance(goal_state)
            frontier.append(node)
            frontier.sort(key=Node.get_manhattan)

        # printing info and setting the limitation
        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')
        if counter > 20000:
            return "NO Answer In Proper Time", 20000
