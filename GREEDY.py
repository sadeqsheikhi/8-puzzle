from Node import Node


def greedy(init, goal_state):
    frontier = [init]
    counter = 0
    # explored = []
    while True:
        if len(frontier) == 0:
            return False

        temp = frontier.pop(0)
        if temp.state == goal_state:
            return temp, counter
        # explored.append(temp)

        children = temp.generate_children()
        for node in children:
            if node == temp.parent:
                continue
            node.manhattan_distance(goal_state)
            frontier.append(node)
            frontier.sort(key=Node.get_manhattan)

        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')
        if counter > 20000:
            return "NO Answer In Proper Time", 20000
