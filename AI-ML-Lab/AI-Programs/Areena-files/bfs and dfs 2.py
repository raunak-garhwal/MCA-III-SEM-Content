from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                stack.extend(reversed(self.graph[node]))
        
        return result
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph[node])
        
        return result

def main():
    graph = Graph()
    
    nodes = input("Enter nodes separated by spaces: ").split()
    edges = eval(input("Enter edges in the form of a dictionary (example: {'node1': ['node2', 'node3'], ...}): "))
    
    for node, neighbors in edges.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)
    
    print("\nGraph Representation:")
    for node in nodes:
        print(f"{node}: {graph.graph[node]}")
    
    while True:
        choice = input("\nEnter 'dfs' for Depth-First Search, 'bfs' for Breadth-First Search, or 'exit' to quit: ")
        
        if choice == 'exit':
            break
        elif choice == 'dfs':
            start_node = input("Enter the starting node for DFS: ")
            if start_node in nodes:
                result = graph.dfs(start_node)
                print("DFS traversal:", result)
            else:
                print("Node not found in graph!")
        elif choice == 'bfs':
            start_node = input("Enter the starting node for BFS: ")
            if start_node in nodes:
                result = graph.bfs(start_node)
                print("BFS traversal:", result)
            else:
                print("Node not found in graph!")
        else:
            print("Invalid choice. Please enter 'dfs', 'bfs', or 'exit'.")

if __name__ == "__main__":
    main()
