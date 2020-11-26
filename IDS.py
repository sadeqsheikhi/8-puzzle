def ids(init, goal_state):
    iteration = 0
    counter = 0
    while iteration < 20:
        frontier = [init]
        visited = []
        iteration += 1
        print(f'depth: {iteration}')
        while True:
            # checking for empty frontier
            if len(frontier) == 0:
                break

            temp = frontier.pop()
            if temp.state == goal_state:
                return temp, counter
            visited.append(temp)
            visited = visited[0:temp.cost + 1]

            for node in temp.generate_children():
                if node in visited or node.cost > iteration:
                    continue
                frontier.append(node)
            counter += 1

    return "NO Answer In Proper Time", counter
