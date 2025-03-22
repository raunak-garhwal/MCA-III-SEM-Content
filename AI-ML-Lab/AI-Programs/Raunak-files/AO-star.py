import heapq

class Node:
    def __init__(self, name, is_and_node=True):
        self.name = name            # Name of the node
        self.is_and_node = is_and_node  # Whether the node is an AND node (True) or OR node (False)
        self.children = []          # List of child nodes
        self.cost = float('inf')    # Cost to reach the node
        self.parent = None          # Parent node
    
    def add_child(self, child):
        self.children.append(child)
    
    def set_cost(self, cost):
        self.cost = cost


class AOStar:
    def __init__(self, root):
        self.root = root
        self.open_list = []          # Min-heap for A* search
        self.closed_list = set()     # Set for nodes already processed
    
    def search(self):
        # Initialize the root node cost as 0 (root cost is always 0)
        self.root.set_cost(0)
        
        # Add root node to open list (priority queue)
        heapq.heappush(self.open_list, (self.root.cost, self.root))

        while self.open_list:
            # Get the node with the lowest cost
            current_cost, current_node = heapq.heappop(self.open_list)
            
            # Skip nodes that have already been processed
            if current_node in self.closed_list:
                continue
            
            self.closed_list.add(current_node)

            # If it's an OR node, choose the least-cost child
            if not current_node.is_and_node:
                min_cost = float('inf')
                best_child = None
                for child in current_node.children:
                    if child.cost < min_cost:
                        min_cost = child.cost
                        best_child = child
                current_node.set_cost(min_cost)
                print(f"Processed OR node: {current_node.name}, chosen child: {best_child.name}")
            
            # If it's an AND node, sum up the costs of all child paths
            else:
                total_cost = 0
                for child in current_node.children:
                    total_cost += child.cost
                current_node.set_cost(total_cost)
                print(f"Processed AND node: {current_node.name}, total cost: {total_cost}")
            
            # Process child nodes and add to open list for further evaluation
            for child in current_node.children:
                if child not in self.closed_list:
                    heapq.heappush(self.open_list, (child.cost, child))
                    child.set_cost(current_cost + child.cost)  # Calculate cost to reach the child

        return self.root.cost


# Function to get user input for creating the task structure
def get_user_input():
    nodes = {}
    num_nodes = int(input("Enter the number of nodes: "))
    
    # Get node details from user input
    for _ in range(num_nodes):
        name = input("Enter the node name: ")
        is_and_node = input(f"Is node '{name}' an AND node? (yes/no): ").strip().lower() == 'yes'
        nodes[name] = Node(name, is_and_node)
    
    # Set up relationships between nodes (parent-child)
    for node_name in nodes:
        print(f"\nEnter children for node '{node_name}' (leave blank if no children):")
        while True:
            child_name = input("Enter a child node name (or press Enter to stop): ")
            if child_name == "":
                break
            if child_name in nodes:
                nodes[node_name].add_child(nodes[child_name])
            else:
                print(f"Node '{child_name}' does not exist.")
    
    # Set costs for nodes
    for node_name in nodes:
        cost = float(input(f"Enter the cost for node '{node_name}': "))
        nodes[node_name].set_cost(cost)
    
    # Return the root node (assumed to be the first node in the list)
    return nodes[list(nodes.keys())[0]]


if __name__ == "__main__":
    # Get user input for nodes and relationships
    root = get_user_input()

    # Perform AO* search
    ao_star = AOStar(root)
    result = ao_star.search()

    # Print result (cost of the solution)
    print(f"\nFinal cost to complete all tasks: {result}")




"""
Enter the number of nodes: 5
Enter the node name: Start
Is node 'Start' an AND node? (yes/no): no
Enter the node name: Task A
Is node 'Task A' an AND node? (yes/no): yes
Enter the node name: Task B
Is node 'Task B' an AND node? (yes/no): yes
Enter the node name: Subtask 1
Is node 'Subtask 1' an AND node? (yes/no): no
Enter the node name: Subtask 2
Is node 'Subtask 2' an AND node? (yes/no): no

Enter children for node 'Start' (leave blank if no children):
Enter a child node name (or press Enter to stop): Task A
Enter a child node name (or press Enter to stop): Task B
Enter a child node name (or press Enter to stop):

Enter children for node 'Task A' (leave blank if no children):
Enter a child node name (or press Enter to stop): Subtask 1
Enter a child node name (or press Enter to stop): Subtask 2
Enter a child node name (or press Enter to stop):

Enter children for node 'Task B' (leave blank if no children):
Enter a child node name (or press Enter to stop): Subtask 1
Enter a child node name (or press Enter to stop):

Enter children for node 'Subtask 1' (leave blank if no children):
Enter a child node name (or press Enter to stop):

Enter children for node 'Subtask 2' (leave blank if no children):
Enter a child node name (or press Enter to stop):

Enter the cost for node 'Start': 0
Enter the cost for node 'Task A': 10
Enter the cost for node 'Task B': 5
Enter the cost for node 'Subtask 1': 2
Enter the cost for node 'Subtask 2': 3

Processed OR node: Start, chosen child: Task A
Processed AND node: Task A, total cost: 10
Processed OR node: Task B, chosen child: Subtask 1
Processed AND node: Task B, total cost: 7

Final cost to complete all tasks: 10
"""