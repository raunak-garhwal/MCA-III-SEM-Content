graph = {}

node_count = int(input("How many nodes you want to enter: "))
for key in range(node_count):
    node = input("Enter Node: ")
    neighbours = input("Enter neighbours of above node (separated by spaces): ").split()
    graph[node] = neighbours

print("Graph :", graph)


def bfs(graph, start):
    visited = set()  # Set to track visited nodes
    queue = [start]  # Initialize queue with the starting node

    while queue:
        node = queue.pop(0)  # Pop the first node (FIFO)
        
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node, end=' ')  # Process the node (here we just print it)
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


n = input("Enter Node to Traverse: ")

print(f"BFS Traversal from node {n}:")
bfs(graph, n)
