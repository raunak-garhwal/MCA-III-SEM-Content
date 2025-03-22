import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent  # Parent node in the path
        self.g = g            # Cost from start node to current node
        self.h = h            # Heuristic cost from current node to goal
        self.f = g + h        # Total cost (g + h)

    def __lt__(self, other):
        # This is required for comparison in the priority queue (heap)
        return self.f < other.f

def a_star_algorithm(start, goal, graph, heuristic):
    # Open list (priority queue) and closed list
    open_list = []
    closed_list = set()
    
    # Start node
    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)
    
    # Dictionary to keep track of the best path to each node
    came_from = {}
    came_from[start] = None

    while open_list:
        current_node = heapq.heappop(open_list)

        # If goal is reached, reconstruct the path
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_list.add(current_node.name)

        # Check neighbors
        for neighbor, cost in graph[current_node.name]:
            if neighbor in closed_list:
                continue

            g_cost = current_node.g + cost
            h_cost = heuristic[neighbor]
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

            # If the neighbor is not in the open list, add it
            if not any(open_node.name == neighbor_node.name and open_node.f <= neighbor_node.f for open_node in open_list):
                heapq.heappush(open_list, neighbor_node)
                came_from[neighbor] = current_node.name

    return None  # No solution found

def get_user_input():
    # Get graph structure (nodes and edges with costs)
    graph = {}
    nodes = input("Enter the nodes separated by spaces: ").split()

    for node in nodes:
        graph[node] = []
    
    for node in nodes:
        print(f"\nEnter neighbors for node '{node}' (format: neighbor1 cost1, neighbor2 cost2, ...):")
        neighbors_input = input("Enter neighbors and their costs (or leave blank if none): ").strip()
        if neighbors_input:
            neighbors = neighbors_input.split(', ')
            for neighbor in neighbors:
                neighbor_name, cost = neighbor.split()
                graph[node].append((neighbor_name, int(cost)))

    # Get heuristic values
    heuristic = {}
    print("\nEnter heuristic values (estimated cost from each node to the goal):")
    for node in nodes:
        h_value = int(input(f"Enter heuristic for node '{node}': "))
        heuristic[node] = h_value

    # Get start and goal nodes
    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    return start, goal, graph, heuristic

def main():
    # Get user input
    start, goal, graph, heuristic = get_user_input()

    # Running the A* algorithm
    path = a_star_algorithm(start, goal, graph, heuristic)

    if path:
        print("\nPath found:", path)
    else:
        print("\nNo path found")

if __name__ == "__main__":
    main()


"""

Enter the nodes separated by spaces: A B C D

Enter neighbors for node 'A' (format: neighbor1 cost1, neighbor2 cost2, ...):
Enter neighbors and their costs (or leave blank if none): B 1, C 4

Enter neighbors for node 'B' (format: neighbor1 cost1, neighbor2 cost2, ...):
Enter neighbors and their costs (or leave blank if none): A 1, C 2, D 5

Enter neighbors for node 'C' (format: neighbor1 cost1, neighbor2 cost2, ...):
Enter neighbors and their costs (or leave blank if none): A 4, B 2, D 1

Enter neighbors for node 'D' (format: neighbor1 cost1, neighbor2 cost2, ...):
Enter neighbors and their costs (or leave blank if none): B 5, C 1

Enter heuristic values (estimated cost from each node to the goal):
Enter heuristic for node 'A': 7
Enter heuristic for node 'B': 6
Enter heuristic for node 'C': 2
Enter heuristic for node 'D': 0

Enter the start node: A
Enter the goal node: D

Path found: ['A', 'B', 'C', 'D']
"""