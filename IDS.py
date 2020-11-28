def ids(init, goal_state):
    iteration, counter = 0, 0

    # adding limitation to the number of iterations
    while iteration < 19:
        frontier, visited = [init], []
        iteration += 1
        print(f'depth: {iteration}')

        # doing each iteration in here using dfs
        while True:
            # checking for empty frontier
            if len(frontier) == 0:
                break

            # getting element out of frontier
            temp = frontier.pop()
            if temp.state == goal_state:
                return temp, counter
            visited.append(temp)
            visited = visited[0:temp.cost + 1]

            # adding valid children to the frontier
            for node in temp.generate_children():
                if node in visited or node.cost > iteration:
                    continue
                frontier.append(node)

            counter += 1

    return "NO Answer In Proper Time", counter
