# Function to check if the current state is the goal state
def is_goal_state(state, goal_state):
    return state == goal_state

# Function to generate possible moves (up, down, left, right)
def get_possible_moves(state):
    moves = []
    # Find the position of the blank space (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    # Directions to move the blank space
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Create a new state by swapping the blank space with the adjacent tile
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append(new_state)
    return moves


def bfs(initial_state, goal_state):
    # Create a queue for BFS and a set to track visited states
    queue = [(initial_state, [])]
    visited = set()

    # Add the initial state to the visited set
    visited.add(tuple(map(tuple, initial_state)))

    while queue:
        current_state, path = queue.pop(0)

        # If we reach the goal state, return the solution path
        if is_goal_state(current_state, goal_state):
            return path

        # Generate the possible moves from the current state
        for next_state in get_possible_moves(current_state):
            next_state_tuple = tuple(map(tuple, next_state))
            if next_state_tuple not in visited:
                visited.add(next_state_tuple)
                queue.append((next_state, path + [next_state]))

    return None  # No solution found

# Function to print the puzzle state in a readable format
def print_state(state):
    for row in state:
        print(row)
    print()

# Function to get user input for a 3x3 matrix
def get_user_input(message):
    print(message)
    state = []
    for i in range(3):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        state.append(row)
    return state

# Main function
def main():
    initial_state = get_user_input("Enter the initial state of the puzzle (3x3 matrix with numbers 0-8):")
    goal_state = get_user_input("Enter the goal state of the puzzle (3x3 matrix with numbers 0-8):")
    
    solution_path = bfs(initial_state, goal_state)

    if solution_path:
        print("Solution found:")
        for state in solution_path:
            print_state(state)
    else:
        print("No solution found.")

# Entry point for the program
if __name__ == "__main__":
    main()
