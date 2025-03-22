import heapq


class Node:
    def __init__(self, name, cost, heuristic):
        self.name = name
        self.cost = cost  
        self.heuristic = heuristic 
        self.total_cost = cost + heuristic  
        self.parent = None 

    def __lt__(self, other):
        return self.total_cost < other.total_cost  
# AO* Algorithm
def ao_star(start, goal, graph, heuristics):
    open_list = []
    closed_list = set()
    start_node = Node(start, 0, heuristics[start])
    
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

        for neighbor, cost in graph.get(current_node.name, {}).items():
            if neighbor in closed_list:
                continue

            
            g_cost = current_node.cost + cost
            h_cost = heuristics.get(neighbor, 0)
            neighbor_node = Node(neighbor, g_cost, h_cost)
            neighbor_node.parent = current_node

            
            if not any(n.name == neighbor and n.total_cost <= neighbor_node.total_cost for n in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  


def main():
    
    print("Enter the nodes (space-separated):")
    nodes = input().split()

    graph = {}
    for node in nodes:
        graph[node] = {}

    print("Enter the edges (format: node1 node2 cost) and type 'done' when finished:")
    while True:
        edge_input = input()
        if edge_input.lower() == 'done':
            break
        edge = edge_input.split()
        node1, node2, cost = edge[0], edge[1], int(edge[2])
        if node1 in graph:
            graph[node1][node2] = cost
        if node2 in graph:
            graph[node2][node1] = cost  # Assuming undirected graph

    print("Enter the heuristic values for each node (format: node heuristic):")
    heuristics = {}
    for node in nodes:
        h_value = int(input(f"Enter heuristic for {node}: "))
        heuristics[node] = h_value

    print("Enter the start node:")
    start = input().strip()

    print("Enter the goal node:")
    goal = input().strip()

    # Run AO* Algorithm
    path = ao_star(start, goal, graph, heuristics)

    if path:
        print(f"Path from {start} to {goal}: {path}")
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
