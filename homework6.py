from queue import PriorityQueue

def bestfirst(start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((heuristic(start, goal), start, []))
    closed_list = set()
    while not open_list.empty():
        _, current_state, path = open_list.get()
        if current_state in closed_list:
            continue
        closed_list.add(current_state)
        if current_state == goal:
            return path + [current_state]
        for neighbor in get_neighbors(current_state):
            if neighbor not in closed_list:
                open_list.put((heuristic(neighbor, goal), neighbor, path + [current_state]))
    return None

def astar(start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic(start, goal), 0, start, []))
    closed_list = set()
    while not open_list.empty():
        _, g, current_state, path = open_list.get()
        if current_state in closed_list:
            continue
        closed_list.add(current_state)
        if current_state == goal:
            return path + [current_state]
        for neighbor in get_neighbors(current_state):
            if neighbor not in closed_list:
                open_list.put((g + 1 + heuristic(neighbor, goal), g + 1, neighbor, path + [current_state]))
    return None

def get_neighbors(state):
    neighbors = []
    blank_x, blank_y = find_blank(state)
    moves = [("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)]
    for _, dx, dy in moves:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == 0:
                return i, j

def heuristic_h1(state, goal):
    return sum(state[i][j] != goal[i][j] and state[i][j] != 0 for i in range(3) for j in range(3))

def heuristic_h2(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = [(x, y) for x, row in enumerate(goal) for y, val in enumerate(row) if val == state[i][j]][0]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def print_solution(solution, name):
    print(f"\n{name} Solution:")
    for step_num, step in enumerate(solution):
        print(f"Step {step_num}:")
        for row in step:
            print(" ".join(str(cell) if cell != 0 else " " for cell in row))
        print()

start_state = (
    (2, 0, 3),
    (1, 7, 4),
    (8, 6, 5)
)

goal_state = (
    (1, 2, 3),
    (7, 4, 5),
    (8, 0, 6)
)

solution_bfs = bestfirst(start_state, goal_state, heuristic_h1)
solution_astar = astar(start_state, goal_state, heuristic_h2)

if solution_bfs:
    print_solution(solution_bfs, "BestFirst Search")
else:
    print("No solution")

if solution_astar:
    print_solution(solution_astar, "A* Search")
else:
    print("No solution")
