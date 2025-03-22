import random

def generate_matrix(rows, cols):
    """
    Generates and returns a random matrix of size rows x cols with values between 0 and 100.
    """
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

def hill_climbing(matrix, start_x, start_y, max_iterations):
    """
    Hill Climbing algorithm to find the local maximum in a matrix.

    Args:
        matrix (list): The matrix to search.
        start_x (int): Starting row index.
        start_y (int): Starting column index.
        max_iterations (int): Maximum number of iterations.

    Returns:
        tuple: Final position (row, col) and value of the local maximum.
    """
    current_x, current_y = start_x, start_y
    current_value = matrix[current_x][current_y]
    print(f"\nStarting at position ({current_x}, {current_y}) with value: {current_value}")

    for iteration in range(max_iterations):
        # Get neighbors within bounds
        neighbors = [
            (x, y) for x, y in [
                (current_x - 1, current_y),  # Up
                (current_x + 1, current_y),  # Down
                (current_x, current_y - 1),  # Left
                (current_x, current_y + 1)   # Right
            ]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
        ]

        # Find the neighbor with the highest value
        next_x, next_y = max(neighbors, key=lambda pos: matrix[pos[0]][pos[1]], default=(current_x, current_y))
        next_value = matrix[next_x][next_y]

        if next_value <= current_value:
            # Local maximum found
            print(f"\nLocal maximum reached at position ({current_x}, {current_y}) with value: {current_value}")
            break

        # Update current position and value
        current_x, current_y, current_value = next_x, next_y, next_value
        print(f"Iteration {iteration + 1}: Current position = ({current_x}, {current_y}), Value = {current_value}")

    return current_x, current_y, current_value

def get_user_input():
    """
    Gets user input for matrix dimensions, starting position, and max iterations.
    """
    rows = int(input("Enter the number of rows for the matrix: "))
    cols = int(input("Enter the number of columns for the matrix: "))
    start_x = int(input(f"Enter the starting row index (0 to {rows - 1}): "))
    start_y = int(input(f"Enter the starting column index (0 to {cols - 1}): "))
    max_iterations = int(input("Enter the maximum number of iterations: "))
    return rows, cols, start_x, start_y, max_iterations

def main():
    """
    Main function to execute the Hill Climbing algorithm with user inputs.
    """
    print("\nHill Climbing Algorithm for Finding Local Maximum in a Matrix")
    print("-------------------------------------------------------------")

    # Get user input
    rows, cols, start_x, start_y, max_iterations = get_user_input()

    # Generate and display the random matrix
    matrix = generate_matrix(rows, cols)
    print("\nGenerated Matrix:")
    for row in matrix:
        print(" ".join(f"{val:3}" for val in row))

    # Run the Hill Climbing algorithm
    result = hill_climbing(matrix, start_x, start_y, max_iterations)

    # Display the final result
    print(f"\nFinal Result: Position = ({result[0]}, {result[1]}), Maximum Value = {result[2]}")

if __name__ == "__main__":
    main()
