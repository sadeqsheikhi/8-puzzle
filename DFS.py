def dfs(init, goal_state):
    frontier = [init]
    counter = 0
    visited = []
    while True:
        # checking for empty frontier
        if len(frontier) == 0:
            return False

        temp = frontier.pop()
        if temp.state == goal_state:
            return temp, counter
        visited.append(temp)
        visited = visited[0:temp.cost + 1]

        for node in temp.generate_children():
            if node in visited:
                continue
            frontier.append(node)

        counter += 1
        if counter % 1000 == 0:
            print(f'Expanded: {counter}')
        if counter > 10000:
            return "NO Answer In Proper Time", 10000




