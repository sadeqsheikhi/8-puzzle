def bfs(init, goal_state):
    frontier = [init]
    explored = []
    counter = 0
    while True:
        # checking for empty frontier
        if len(frontier) == 0:
            return False

        temp = frontier.pop(0)
        if temp.state == goal_state:
            return temp, counter
        explored.append(temp)

        for node in temp.generate_children():
            if node in explored or node == temp.parent:
                continue
            frontier.append(node)

        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')
        if counter > 10000:
            return "NO Answer In Proper Time", 10000