import random

def generate_matrix(rows, cols):
    """Generates and returns a random matrix of size rows x cols."""
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

def hill_climbing(matrix, start_x, start_y, max_iterations):
    """Hill Climbing algorithm to find the local maximum in a matrix."""
    current_x, current_y = start_x, start_y
    current_value = matrix[current_x][current_y]
    print(f"Starting at position ({current_x}, {current_y}) with value: {current_value}")

    for iteration in range(max_iterations):
        neighbors = [(x, y) for x, y in [(current_x-1, current_y), (current_x+1, current_y), 
                                         (current_x, current_y-1), (current_x, current_y+1)] 
                     if 0 <= x < len(matrix) and 0 <= y < len(matrix[0])]
        
        next_x, next_y = max(neighbors, key=lambda pos: matrix[pos[0]][pos[1]], default=(current_x, current_y))
        next_value = matrix[next_x][next_y]
        
        if next_value <= current_value:
            print(f"Local maximum reached at position ({current_x}, {current_y}) with value: {current_value}")
            break

        current_x, current_y, current_value = next_x, next_y, next_value
        print(f"Iteration {iteration + 1}: Current position = ({current_x}, {current_y}), Value = {current_value}")

    return current_x, current_y, current_value

# Generate a random 5x5 matrix
matrix = generate_matrix(5, 5)

# Print the matrix
print("Matrix:")
for row in matrix:
    print(row)

# Parameters and running the hill climbing algorithm
result = hill_climbing(matrix, random.randint(0, 4), random.randint(0, 4), 100)
print(f"\nFinal result: Position = ({result[0]}, {result[1]}), Maximum Value = {result[2]}")
