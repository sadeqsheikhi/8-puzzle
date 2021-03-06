from Node import Node


def ah2(init, goal_state):
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
        children = temp.generate_children()
        for node in children:
            if node in frontier or node in explored:
                continue

            # inserting to frontier in a sorted way using manhattan_distance heuristic
            node.manhattan_distance(goal_state)
            frontier.append(node)
            frontier.sort(key=Node.get_manhattan_cost)

        # printing info and setting the limitation
        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')
        if counter > 10000:
            return "NO Answer In Proper Time", 10000
