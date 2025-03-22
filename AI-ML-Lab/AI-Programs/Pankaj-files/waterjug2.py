# Define the production rules with associated rule numbers
def water_jug_problem(state):
    x, y = state
    next_states = []

    # Rule 1: Fill jug1
    if x < jug1:
        next_states.append(((jug1, y), "Rule 1: Fill jug1"))
    
    # Rule 2: Fill jug2
    if y < jug2:
        next_states.append(((x, jug2), "Rule 2: Fill jug2"))
    
    # Rule 3: Pour water from jug1 to jug2
    if x > 0 and y < jug2:
        pour = min(x, jug2 - y)
        next_states.append(((x - pour, y + pour), "Rule 3: Pour water from jug1 to jug2"))
    
    # Rule 4: Pour water from jug2 to jug1
    if y > 0 and x < jug1:
        pour = min(y, jug1 - x)
        next_states.append(((x + pour, y - pour), "Rule 4: Pour water from jug2 to jug1"))
    
    # Rule 5: Empty jug1
    if x > 0:
        next_states.append(((0, y), "Rule 5: Empty jug1"))
    
    # Rule 6: Empty jug2
    if y > 0:
        next_states.append(((x, 0), "Rule 6: Empty jug2"))
    
    # Rule 7: Pour from jug2 to jug1 until jug1 is full
    if x + y >= jug1 and y > 0:
        next_states.append(((jug1, y - (jug1 - x)), "Rule 7: Pour from jug2 to jug1 until it's full"))
    
    # Rule 8: Pour from jug1 to jug2 until jug2 is full
    if x + y >= jug2 and x > 0:
        next_states.append(((x - (jug2 - y), jug2), "Rule 8: Pour from jug1 to jug2 until it's full"))
    
    # Rule 9: Pour all from jug2 to jug1
    if x + y <= jug1 and y > 0:
        next_states.append(((x + y, 0), "Rule 9: Pour all from jug2 to jug1"))
    
    # Rule 10: Pour all from jug1 to jug2
    if x + y <= jug2 and x > 0:
        next_states.append(((0, x + y), "Rule 10: Pour all from jug1 to jug2"))
    
    # Rule 11: Specific case (m, n) -> (n, m)
    if x == 0 and y == m:
        next_states.append(((m, 0), "Rule 11: Specific case (m, n) -> (n, m)"))
    
    # Rule 12: Specific case (m, y) -> (0, y)
    if x == m:
        next_states.append(((0, y), "Rule 12: Specific case (m, y) -> (0, y)"))
    
    return next_states

# Breadth-First Search to find the solution
def water_jug_bfs(start_state, goal_state):
    queue = [(start_state, [])]  # queue contains (state, path)
    visited = set([start_state])  # visited states
    
    while queue:
        current_state, path = queue.pop(0)

        # If both Jug1 and Jug2 match the goal state, return the path with rules
        if current_state == goal_state:
            return path + [current_state]
        
        # Generate next states from current state and check if they are visited
        for next_state, rule in water_jug_problem(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(current_state, rule)]))
    
    return None

# Input: Jug capacities and goal state
jug1 = int(input("Enter the capacity of Jug1: "))
jug2 = int(input("Enter the capacity of Jug2: "))
m = int(input("Enter the goal capacity of Jug1: "))
n = int(input("Enter the goal capacity of Jug2: "))

start = (0, 0)
goal = (m, n)  
solution = water_jug_bfs(start, goal)

# Output the solution path and corresponding rules
if solution:
    print("Solution found:")
    for state, rule in solution:
        print(f"State: {state} -> {rule}")
else:
    print("No solution found.")
