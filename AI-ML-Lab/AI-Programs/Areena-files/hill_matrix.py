import random


n = 5


matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(row)


def get_neighbors(i, j, matrix):
    neighbors = []
    
    if i > 0:  # up
        neighbors.append((i - 1, j))
    if i < n - 1:  # down
        neighbors.append((i + 1, j))
    if j > 0:  # left
        neighbors.append((i, j - 1))
    if j < n - 1:  # right
        neighbors.append((i, j + 1))
    return neighbors


def hill_climb(matrix):
    global_max = -1  
    global_max_position = None
    local_max = -1  
    local_max_position = None

    
    for j in range(n):  # Iterate through each cell in the first row
        i = 0  # We always start from the first row
        current_value = matrix[i][j]

        # Perform hill climbing from the starting point (i, j)
        while True:
            neighbors = get_neighbors(i, j, matrix)

            # Find the neighbor with the highest value
            best_value = current_value
            best_pos = (i, j)

            for ni, nj in neighbors:
                if matrix[ni][nj] > best_value:
                    best_value = matrix[ni][nj]
                    best_pos = (ni, nj)

            # If no better neighbor is found, we have reached a local maximum
            if best_pos == (i, j):
                break

            # Move to the best neighbor
            i, j = best_pos
            current_value = best_value

        # Check if the current local maximum is the new global maximum
        if current_value > global_max:
            global_max = current_value
            global_max_position = (i, j)

        # Track the highest local maximum encountered
        if current_value > local_max:
            local_max = current_value
            local_max_position = (i, j)

    # Return the global maximum, or the best local maximum if no global max found
    if global_max_position:
        return global_max, global_max_position
    else:
        return local_max, local_max_position


print("Generated 5x5 Matrix:")
print_matrix(matrix)


global_max, global_max_position = hill_climb(matrix)


if global_max_position:
    print(f"\nGlobal Maximum Found: {global_max} at position {global_max_position}")
else:
    print(f"\nNo global maximum found, local maximum found: {global_max} at position {global_max_position}")
