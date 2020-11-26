from Node import Node


def ah2(init, goal_state):
    frontier = [init]
    counter = 0
    explored = []
    while True:
        if len(frontier) == 0:
            return False

        temp = frontier.pop(0)
        if temp.state == goal_state:
            return temp, counter
        explored.append(temp)

        children = temp.generate_children()
        for node in children:
            if node in frontier or node in explored:
                continue
            node.manhattan_distance(goal_state)
            frontier.append(node)
            frontier.sort(key=Node.get_manhattan_cost)

        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')
        if counter > 10000:
            return "NO Answer In Proper Time", 10000
