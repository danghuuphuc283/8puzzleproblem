from queue import Queue, PriorityQueue

def print_state(state):
    for row in state:
        print(" ".join(str(cell) if cell != 0 else " " for cell in row))
    print()

def is_goal(state, goal):
    return state == goal

def find_blank(state):
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell == 0:  # 0 đại diện cho ô trống
                return i, j

def move(state, direction):
    x, y = find_blank(state)
    new_state = [list(row) for row in state]
    if direction == "up" and x > 0:
        new_state[x][y], new_state[x-1][y] = new_state[x-1][y], new_state[x][y]
    elif direction == "down" and x < 2:
        new_state[x][y], new_state[x+1][y] = new_state[x+1][y], new_state[x][y]
    elif direction == "left" and y > 0:
        new_state[x][y], new_state[x][y-1] = new_state[x][y-1], new_state[x][y]
    elif direction == "right" and y < 2:
        new_state[x][y], new_state[x][y+1] = new_state[x][y+1], new_state[x][y]
    return tuple(tuple(row) for row in new_state)

def get_neighbors(state):
    directions = ["up", "down", "left", "right"]
    neighbors = []
    for direction in directions:
        neighbors.append(move(state, direction))
    return neighbors

#BFS
def bfs(start, goal):
    visited = set()
    queue = Queue()
    queue.put((start, []))
    while not queue.empty():
        current_state, path = queue.get()
        if current_state in visited:
            continue
        visited.add(current_state)
        if is_goal(current_state, goal):
            return path + [current_state]
        for neighbor in get_neighbors(current_state):
            queue.put((neighbor, path + [current_state]))
    return None

#DFS
def dfs(start, goal, depth=0, max_depth=5):
    visited = set()
    stack = [(start, [])]
    while stack:
        current_state, path = stack.pop()
        if len(path) > max_depth:
            continue
        if current_state in visited:
            continue
        visited.add(current_state)
        if is_goal(current_state, goal):
            return path + [current_state]
        for neighbor in get_neighbors(current_state):
            stack.append((neighbor, path + [current_state]))
    return None

#UCS
def ucs(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start, []))
    while not pq.empty():
        cost, current_state, path = pq.get()
        if current_state in visited:
            continue
        visited.add(current_state)
        if is_goal(current_state, goal):
            return path + [current_state]
        for neighbor in get_neighbors(current_state):
            pq.put((cost + 1, neighbor, path + [current_state]))
    return None

#ID
def iterative_deepening(start, goal, max_depth=5):
    for depth in range(max_depth + 1):
        result = dfs(start, goal, max_depth=depth)
        if result is not None:
            return result
    return None


def print_solution(solution):
    if not solution:
        print("Không tìm thấy giải pháp.")
        return
    print(f"Số bước: {len(solution) - 1}")
    for i, state in enumerate(solution):
        print(f"Bước {i}:")
        print_state(state)

# Main
if __name__ == "__main__":
    start_state = (
        (2, 3, 7),
        (1, 4, 5),
        (8, 0, 6) 
    )
    goal_state = (
        (1, 2, 3),
        (7, 4, 0),
        (8, 5, 6)
    )

    print("BFS:")
    print_solution(bfs(start_state, goal_state))

    print("DFS:")
    print_solution(dfs(start_state, goal_state))

    print("UCS:")
    print_solution(ucs(start_state, goal_state))

    print("Iterative Deepening:")
    print_solution(iterative_deepening(start_state, goal_state))

