moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def print_state(state): 
    for row in state: print(" ".join(map(str, row)))

def bfs(initial, goal):
    queue, visited = [(initial, [])], {tuple(map(tuple, initial))}
    while queue:
        state, path = queue.pop(0)
        if state == goal: return path
        x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                t_state = tuple(map(tuple, new_state))
                if t_state not in visited:
                    visited.add(t_state)
                    queue.append((new_state, path + [new_state]))
    return None

def get_input():
    while True:
        initial = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(3)]
        if any(0 in row for row in initial): break
        print("Error: Initial state must contain a 0 (blank space).")
    goal = [list(map(int, input(f"Enter goal row {i+1}: ").split())) for i in range(3)]
    return initial, goal

def main():
    initial, goal = get_input()
    path = bfs(initial, goal)
    if path:
        print("Solution Found")
        for step in path:
            print()
            print_state(step)
    else: print("No solution exists.")

if __name__ == "__main__":
    main()
