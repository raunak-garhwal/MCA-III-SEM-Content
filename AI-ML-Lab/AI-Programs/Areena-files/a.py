import heapq

class Node:
    def __init__(self, name, g=0, h=0, parent=None):
        self.name = name   
        self.g = g         
        self.h = h         
        self.f = g + h     
        self.parent = parent  

    def __lt__(self, other):
        return self.f < other.f  


def astar(graph, heuristics, start, goal):
    open_list = []  
    closed_list = set()  
    
    
    start_node = Node(start, g=0, h=heuristics[start])
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)  
        
        if current_node.name == goal:
            
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  

        closed_list.add(current_node.name)
        
        
        for neighbor, cost in graph[current_node.name]:
            if neighbor in closed_list:
                continue

            g_cost = current_node.g + cost
            h_cost = heuristics.get(neighbor, 0) 
            neighbor_node = Node(neighbor, g=g_cost, h=h_cost, parent=current_node)

            
            if not any(n.name == neighbor and n.f <= neighbor_node.f for n in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  


def get_graph_input():
    
    num_nodes = int(input("Enter the number of nodes: "))
    
    
    graph = {}
    for _ in range(num_nodes):
        node = input("Enter node name: ").strip()
        graph[node] = []
    
   
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        node1, node2, cost = input("Enter an edge (node1 node2 cost): ").split()
        cost = int(cost)
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))  
    
    
    heuristics = {}
    for node in graph:
        heuristics[node] = int(input(f"Enter heuristic value for {node}: "))
    
    
    start_node = input("Enter start node: ").strip()
    goal_node = input("Enter goal node: ").strip()

    return graph, heuristics, start_node, goal_node


def main():
    graph, heuristics, start, goal = get_graph_input()
    
    print("\nGraph:", graph)
    print("Heuristics:", heuristics)
    
    
    path = astar(graph, heuristics, start, goal)

    if path:
        print(f"\nShortest path from {start} to {goal}:")
        print(" -> ".join(path))
    else:
        print(f"\nNo path found from {start} to {goal}")

if __name__ == "__main__":
    main()
