def ao_star(start, goal):
    open_list = [(abs(start[0] - goal[0]) + abs(start[1] - goal[1]), start, [])]  # f = h
    closed_list = set()
    
    while open_list:
        _, state, path = open_list.pop(0)
        if state == goal: return path + [state]
        if state not in closed_list:
            closed_list.add(state)
            for nx, ny in [(state[0] + dx, state[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                open_list.append((abs(nx - goal[0]) + abs(ny - goal[1]), (nx, ny), path + [state]))
            open_list.sort()
    return None

def get_input():
    return tuple(map(int, input("Enter starting coordinates (x y): ").split())), \
           tuple(map(int, input("Enter goal coordinates (x y): ").split()))

def main():
    start, goal = get_input()
    path = ao_star(start, goal)
    print(f"Path found by AO*: {path}" if path else "No solution found.")

if __name__ == "__main__":
    main()
