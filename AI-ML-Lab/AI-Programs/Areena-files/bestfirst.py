import heapq


def best_first_search(graph, heuristics, start, goal):
    
    open_list = []
    
    
    visited = set()

    
    heapq.heappush(open_list, (heuristics[start], start))

    
    parent = {start: None}

    while open_list:
        
        _, current_node = heapq.heappop(open_list)

        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path
        
       
        visited.add(current_node)

        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))
                
                parent[neighbor] = current_node

    
    return None



def take_input():
    
    n = int(input("Enter the number of nodes: "))
    
    graph = {}
    for _ in range(n):
        node = input("Enter the node name: ")
        neighbors = input(f"Enter neighbors for {node} (comma separated): ").split(",")
        graph[node] = [neighbor.strip() for neighbor in neighbors]
    
    heuristics = {}
    for node in graph:
        heuristics[node] = int(input(f"Enter the heuristic value for node {node}: "))
    
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    return graph, heuristics, start, goal



def main():
    
    graph, heuristics, start, goal = take_input()

    
    path = best_first_search(graph, heuristics, start, goal)
    
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found from start to goal.")

# Run the program
if __name__ == "__main__":
    main()
