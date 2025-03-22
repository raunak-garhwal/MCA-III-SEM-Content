import random

def print_board(board):
    for row in board: print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    return all(board[start_row + i][start_col + j] != num for i in range(3) for j in range(3))

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board): return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0]*9 for _ in range(9)]
    solve_sudoku(board)
    for _ in range(40):  # Adjust difficulty by changing this number
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0: row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

sudoku_board = generate_sudoku()

print("Generated Sudoku Puzzle:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists")
