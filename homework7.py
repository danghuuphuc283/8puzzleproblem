def hill_climbing(start, goal, heuristic):
    current_state = start
    path = [current_state]
    visited = set()
    visited.add(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break
        next_state = None
        next_heuristic = float('inf')
        for neighbor in neighbors:
            if neighbor not in visited:
                h_value = heuristic(neighbor, goal)
                if h_value < next_heuristic:
                    next_state = neighbor
                    next_heuristic = h_value
        if next_heuristic >= heuristic(current_state, goal):
            break

        current_state = next_state
        path.append(current_state)
        visited.add(current_state)

        if current_state == goal:
            return path
    
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

def print_solution(solution):
    if solution:
        print("Solution:")
        for step_num, step in enumerate(solution):
            print(f"Step {step_num}:")
            for row in step:
                print(" ".join(str(cell) if cell != 0 else " " for cell in row))
            print()
    else:
        print("No solution")

start_state = (
    (2, 3, 7),
    (1, 6, 8),
    (0, 5, 4)
)

goal_state = (
    (1, 2, 3),
    (7, 4, 5),
    (8, 0, 6)
)

solution = hill_climbing(start_state, goal_state, heuristic_h1)
print_solution(solution)

