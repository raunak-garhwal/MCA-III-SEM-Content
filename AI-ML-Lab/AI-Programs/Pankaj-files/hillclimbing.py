import random

def generate_random_matrix(n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def evaluate(matrix, fitness_type="sum"):
    if fitness_type == "sum":
        return sum(sum(row) for row in matrix)
    elif fitness_type == "product":
        product = 1
        for row in matrix:
            for val in row:
                product *= val
        return product
    elif fitness_type == "mean":
        total_elements = len(matrix) * len(matrix[0])
        total_sum = sum(sum(row) for row in matrix)
        return total_sum / total_elements
    else:
        raise ValueError("Unsupported fitness type")

def generate_neighbors(matrix, n):
    neighbors = []
    for i in range(n):
        for j in range(n):
            neighbor = [row[:] for row in matrix] 
            neighbor[i][j] = random.randint(1, 100) 
            neighbors.append(neighbor)
    return neighbors

def hill_climb(n, fitness_type="sum", max_iterations=1000, tolerance=0.01):
    current = generate_random_matrix(n)
    current_score = evaluate(current, fitness_type)
    
    iteration = 0
    best_score = current_score
    best_matrix = current
    
    while iteration < max_iterations:
        neighbors = generate_neighbors(current, n)
        best_neighbor = None
        best_neighbor_score = current_score
        
        for neighbor in neighbors:
            score = evaluate(neighbor, fitness_type)
            if score > best_neighbor_score: 
                best_neighbor = neighbor
                best_neighbor_score = score
        
        if best_neighbor_score <= best_score - tolerance:
            best_matrix = best_neighbor
            best_score = best_neighbor_score
        
        if best_score == current_score:
            break
        
        current = best_neighbor
        current_score = best_neighbor_score
        
        iteration += 1
        
    return best_matrix, best_score, iteration

def get_user_input():
    n = int(input("Enter the size of the matrix (e.g., 5 for 5x5): "))
    fitness_type = input("Enter the fitness function (sum, product, mean): ").strip().lower()
    return n, fitness_type

if __name__ == "__main__":
    n, fitness_type = get_user_input()
    solution, solution_score, iterations = hill_climb(n, fitness_type)
    
    print("\nOptimal Matrix Found:")
    for row in solution:
        print(row)
    print("\nScore:", solution_score)
    print("Iterations:", iterations)
