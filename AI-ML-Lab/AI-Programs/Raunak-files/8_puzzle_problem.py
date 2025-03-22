from collections import deque

# Moves represent Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))
    print()

def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def generate_successors(state):
    successors = []
    zero_row, zero_col = find_zero(state)
    for dr, dc in moves:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < len(state) and 0 <= new_col < len(state[0]):
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            successors.append(new_state)
    return successors

def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = set()
    visited.add(tuple(map(tuple, initial)))

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [goal]

        for successor in generate_successors(state):
            state_tuple = tuple(map(tuple, successor))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((successor, path + [successor]))

    return None

def get_input():
    while True:
        print("\nEnter the Initial Puzzle :-")
        initial = [list(map(int, input(f"Enter row {i+1} of initial state: ").split())) for i in range(3)]
        if any(0 in row for row in initial):
            break
        print("Error: Initial state must contain a 0 (blank space).")

    print("\nEnter the Goal Puzzle :-")
    goal = [list(map(int, input(f"Enter row {i+1} of goal state: ").split())) for i in range(3)]
    return initial, goal

def main():
    initial, goal = get_input()
    print("\nInitial State:")
    print_state(initial)
    print("Goal State:")
    print_state(goal)

    solution = bfs(initial, goal)

    if solution:
        print("Solution Found:")
        for step in solution:
            print_state(step)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
