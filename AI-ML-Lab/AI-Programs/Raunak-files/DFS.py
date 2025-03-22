graph = {}

node_count = int(input("How many nodes you want to enter: "))
for key in range(node_count):
    node = input("Enter Node: ")
    neighbours = input("Enter neighbours of above node (separated by spaces): ").split()
    graph[node] = neighbours

print("Graph :", graph)


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set the first time

    # Mark the node as visited
    visited.add(node)
    print(node, end=' ')  # Process the node (e.g., print it)

    # Recursively visit each unvisited neighbor
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


n = input("Enter the node to traverse : ")
print(f"DFS Traversal from node-{n}:")
dfs(graph, n)
