import heapq

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state  
        self.parent = parent
        self.cost = cost 
    
    def __lt__(self, other):
        return self.cost < other.cost  

def best_first_search(start_state, goal_state, heuristic_function):
  
    open_list = []
    
    start_node = Node(start_state, None, heuristic_function(start_state, goal_state))
    
    heapq.heappush(open_list, start_node)
    
    visited = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1] 

        visited.add(current_node.state)
        
        neighbors = get_neighbors(current_node.state)

        for neighbor in neighbors:
            if neighbor not in visited:
                cost = heuristic_function(neighbor, goal_state)
                neighbor_node = Node(neighbor, current_node, cost)
                heapq.heappush(open_list, neighbor_node)
    
    return None  

def heuristic_function(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(state):
    x, y = state
    neighbors = [
        (x+1, y), (x-1, y), (x, y+1), (x, y-1) 
    ]
    return neighbors

if __name__ == "__main__":
    start = (0, 0) 
    goal = (3, 3)  
    
    path = best_first_search(start, goal, heuristic_function)
    
    if path:
        print(f"Path found: {path}")
    else:
        print("No path found")
