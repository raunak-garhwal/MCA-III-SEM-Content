from collections import deque


def fill_jug(x, y, jug_capacity, jug2_capacity):
    if x < jug_capacity:
        return (jug_capacity, y)
    return None

def fill_jug2(x, y, jug_capacity, jug2_capacity):
    if y < jug2_capacity:
        return (x, jug2_capacity)
    return None

def pour_from_jug1_to_jug2(x, y, jug_capacity, jug2_capacity):
    if x > 0 and y < jug2_capacity:
        transfer_amount = min(x, jug2_capacity - y)
        return (x - transfer_amount, y + transfer_amount)
    return None

def pour_from_jug2_to_jug1(x, y, jug_capacity, jug2_capacity):
    if y > 0 and x < jug_capacity:
        transfer_amount = min(y, jug_capacity - x)
        return (x + transfer_amount, y - transfer_amount)
    return None

def empty_jug1(x, y, jug_capacity, jug2_capacity):
    if x > 0:
        return (0, y)
    return None

def empty_jug2(x, y, jug_capacity, jug2_capacity):
    if y > 0:
        return (x, 0)
    return None

def pour_jug2_into_jug1_until_full(x, y, jug_capacity, jug2_capacity):
    if x + y >= jug_capacity and y > 0:
        transfer_amount = jug_capacity - x
        return (jug_capacity, y - transfer_amount)
    return None

def pour_jug1_into_jug2_until_full(x, y, jug_capacity, jug2_capacity):
    if x + y >= jug2_capacity and x > 0:
        transfer_amount = jug2_capacity - y
        return (x - transfer_amount, jug2_capacity)
    return None

def pour_all_from_jug2_to_jug1(x, y, jug_capacity, jug2_capacity):
    if x + y <= jug_capacity and y > 0:
        return (x + y, 0)
    return None

def pour_all_from_jug1_to_jug2(x, y, jug_capacity, jug2_capacity):
    if x + y <= jug2_capacity and x > 0:
        return (0, x + y)
    return None


def get_possible_actions(x, y, jug_capacity, jug2_capacity):
    actions = [
        fill_jug,
        fill_jug2,
        pour_from_jug1_to_jug2,
        pour_from_jug2_to_jug1,
        empty_jug1,
        empty_jug2,
        pour_jug2_into_jug1_until_full,
        pour_jug1_into_jug2_until_full,
        pour_all_from_jug2_to_jug1,
        pour_all_from_jug1_to_jug2
    ]
    
    valid_actions = []
    for action in actions:
        new_state = action(x, y, jug_capacity, jug2_capacity)
        if new_state:
            valid_actions.append(new_state)
    return valid_actions


def bfs(initial_state, goal_state, jug_capacity, jug2_capacity):
    
    queue = deque([(initial_state, [])])  
    
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        x, y = current_state
        
        
        if current_state == goal_state:
            return path
        
        
        valid_actions = get_possible_actions(x, y, jug_capacity, jug2_capacity)
        for next_state in valid_actions:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None  


def main():
    # User inputs jug capacities
    jug_capacity = int(input("Enter the capacity of the first jug (e.g., 4 liters): "))
    jug2_capacity = int(input("Enter the capacity of the second jug (e.g., 3 liters): "))
    
    # User inputs initial state of both jugs
    x = int(input(f"Enter the initial amount of water in the first jug (0-{jug_capacity}): "))
    y = int(input(f"Enter the initial amount of water in the second jug (0-{jug2_capacity}): "))
    initial_state = (x, y)
    
    # User inputs goal state
    goal_x = int(input(f"Enter the goal amount of water in the first jug (0-{jug_capacity}): "))
    goal_y = int(input(f"Enter the goal amount of water in the second jug (0-{jug2_capacity}): "))
    goal_state = (goal_x, goal_y)
    
    
    solution_path = bfs(initial_state, goal_state, jug_capacity, jug2_capacity)
    
    if solution_path:
        print("Solution found! Steps to reach the goal state:")
        for step in solution_path:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
