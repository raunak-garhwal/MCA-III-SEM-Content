import heapq


GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  


def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue  
        goal_row, goal_col = divmod(state[i] - 1, 3)
        current_row, current_col = divmod(i, 3)
        distance += abs(goal_row - current_row) + abs(goal_col - current_col)
    return distance


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


def a_star(start_state):
    
    pq = []
    
    heapq.heappush(pq, (manhattan_distance(start_state), 0, start_state, []))
    
    visited = set()
    visited.add(start_state)

    while pq:
        f, g, state, path = heapq.heappop(pq)

        
        if state == GOAL_STATE:
            return path + [state]

        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                h = manhattan_distance(neighbor)
                heapq.heappush(pq, (g + 1 + h, g + 1, neighbor, path + [state]))

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

 
def main():
    start_state = get_user_input()  
    print(f"Initial state: {start_state}")
    
    solution = a_star(start_state)

    if solution:
        print("Solution found:")
        for step in solution:
            print(step)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
