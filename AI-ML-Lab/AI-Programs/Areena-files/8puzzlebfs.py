from collections import deque


GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  


def get_neighbors(state):
    empty_index = state.index(0)  
    row, col = divmod(empty_index, 3)  
    neighbors = []

    for move in MOVES:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col 
            new_state = list(state)
            new_state[empty_index], new_state[new_index] = new_state[new_index], new_state[empty_index]
            neighbors.append(tuple(new_state))

    return neighbors


def bfs(start_state):
   
    queue = deque([(start_state, [])])
    
    visited = set()
    visited.add(start_state)

    while queue:
        state, path = queue.popleft()

        
        if state == GOAL_STATE:
            return path + [state]

       
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))

    return None 


def get_user_input():
    while True:
        user_input = input("Enter the 8-puzzle initial state as a space-separated list of numbers (0 represents the empty space): ")
       
        try:
            state = tuple(map(int, user_input.split()))
            if len(state) == 9 and set(state) == {0, 1, 2, 3, 4, 5, 6, 7, 8}:
                return state
            else:
                print("Invalid input! Please enter exactly 9 numbers, with each number between 0 and 8, and no repetitions.")
        except ValueError:
            print("Invalid input! Please enter space-separated integers.")

# Main function to run the BFS solver with user input
def main():
    start_state = get_user_input()  # Get user input for the initial state
    print(f"Initial state: {start_state}")
    
    solution = bfs(start_state)

    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
