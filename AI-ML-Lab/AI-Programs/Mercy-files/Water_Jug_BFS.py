def water_jug_bfs(capacity, goal):
    queue, visited = [(0, 0, [])], {(0, 0)}
    
    while queue:
        x, y, path = queue.pop(0)
        if x == goal or y == goal:
            print("Solution path:")
            for step in path + [(x, y)]:
                print(f"Jug1: {step[0]}, Jug2: {step[1]}")
            return
        
        next_states = [
            (capacity[0], y), (x, capacity[1]), (0, y), (x, 0), 
            (x - min(x, capacity[1] - y), y + min(x, capacity[1] - y)), 
            (x + min(y, capacity[0] - x), y - min(y, capacity[0] - x))
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(x, y)]))
    
    print("No solution found.")

def get_input():
    jug1_capacity, jug2_capacity, goal = int(input("Enter Jug1 capacity: ")), int(input("Enter Jug2 capacity: ")), int(input("Enter goal: "))
    water_jug_bfs((jug1_capacity, jug2_capacity), goal)

get_input()
