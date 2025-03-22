def print_board(board):
    """Utility function to print the chessboard with queens."""
    N = len(board)
    for i in range(N):
        row = ['Q' if x == 1 else '.' for x in board[i]]
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    N = len(board)
    
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row):
    """Utilizes backtracking to solve the N-Queens problem."""
    N = len(board)
    
    # If all queens are placed
    if row == N:
        print_board(board)
        return True

    res = False
    for col in range(N):
        # Check if placing the queen is safe
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1
            
            # Recursively place the queen on the next row
            res = solve_n_queens_util(board, row + 1) or res

            # Backtrack (Remove the queen if placing it doesn't lead to a solution)
            board[row][col] = 0
    
    return res

def solve_n_queens(N):
    """Solve the N-Queens problem using backtracking."""
    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist.")
    else:
        print(f"Solutions for {N}-Queens problem")

queens = int(input("Enter the number of queens : "))
solve_n_queens(queens)
