# 8-PUZZLE 
## Python Implementation Using Informed & Un-informed Searches

This project has been done as university assignment on the artificial intelligence course.
I have tried to comment my code so it's clear what i have done.
dont forget to star me

### Implemented Algorithms
- BFS(Breadth First Search)
- DFS(Depth First Search)
- IDS(Iterative Deepening Search)
- UCS(Uniform Cost Search)
- Greedy Best First Search
- AH1 (A* with missplaced tiles heuristic -- *Consistent*)
- AH2 (A* with manhattan distance hueristic -- *Consistent*)
- AH3 (A* with missplaces tiles * 100 heuristic -- *not admissible*)

### Test Cases
there test cases are stored in main.py file and have been commented out by their difficulty levels.
-- you can also accept user input buy uncommenting the user_input function.

### Solvability
there is a function in utility.py file that checks if the game is solveble or not.
-- this function is called by default when getting inputs so an infinite loop is avoided

### Search Limitations
searches are limited in the amount of nodes they can expand, we may think the game is simple, but in some cases uninformed 
searches can run for hours.
-- you can change the limitation of each algorithm in the associated file


##### note that the AH3 algorithm does not provide optimal solutions, it's just for finding fast answers


-- if you find any problems in the project, contribute you fix