import random

def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def is_valid(board, row, col, num):
    """Checks if placing 'num' at (row, col) is valid according to Sudoku rules."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    return all(board[start_row + i][start_col + j] != num for i in range(3) for j in range(3))

def solve_sudoku(board, step_interval, step_count=0, first_print=True):
    """Solves the Sudoku board using backtracking and prints the board at step intervals."""
    if first_print:  # Print the initial board state
        print("Initial Board State:")
        print_board(board)

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        step_count += 1
                        
                        if step_count % step_interval == 0:
                            print(f"Step {step_count}:")
                            print_board(board)

                        if solve_sudoku(board, step_interval, step_count, first_print=False):
                            return True

                        board[row][col] = 0  # Backtrack
                
                return False  # No valid number found, trigger backtracking
    return True  # Sudoku solved

def generate_sudoku():
    """Generates a valid Sudoku puzzle by solving a blank board and removing numbers."""
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board, step_interval=1000)  # Solve completely to get a valid board
    
    # Remove numbers to create a puzzle
    for _ in range(random.randint(40, 50)):  # Adjust difficulty by changing range
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

# Generate a Sudoku puzzle
sudoku_board = generate_sudoku()
print("Generated Sudoku Puzzle:")
print_board(sudoku_board)

# Ask user for step interval
step_interval = int(input("Enter after how many steps you want to print the board (e.g., 10, 100): "))

# Solve Sudoku with step-by-step display
if solve_sudoku(sudoku_board, step_interval):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists")
