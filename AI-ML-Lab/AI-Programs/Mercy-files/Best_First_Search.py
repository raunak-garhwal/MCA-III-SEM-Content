def bfs(start, goal):
    queue = [(start, [])]
    visited = {start}
    
    while queue:
        state, path = queue.pop(0)
        if state == goal: return path + [state]
        for nx, ny in [(state[0] + dx, state[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [state]))
    return None

def get_input():
    return tuple(map(int, input("Enter starting coordinates (x y): ").split())), \
           tuple(map(int, input("Enter goal coordinates (x y): ").split()))

def main():
    start, goal = get_input()
    path = bfs(start, goal)
    print(f"Path found by BFS: {path}" if path else "No solution found.")

if __name__ == "__main__":
    main()
