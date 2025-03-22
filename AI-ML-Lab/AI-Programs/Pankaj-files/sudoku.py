import random

N = 9
def is_valid(board, row, col, num):
    for x in range(N):
        if board[row][x] == num:
            return False
    
    for x in range(N):
        if board[x][col] == num:
            return False
        
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True
def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True 
    
    row, col = empty

    for num in range(1, N + 1): 
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board): 
                return True

            board[row][col] = 0 

    return False
def find_empty_cell(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return (i, j)
    return None 
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
def input_sudoku():
    board = []
    print("Enter the Sudoku puzzle (use 0 or '.' for empty cells):")
    for i in range(N):
        row = input(f"Enter row {i + 1} (9 numbers separated by spaces): ").strip()
        row_values = [int(x) if x != '.' else 0 for x in row.split()]
        board.append(row_values)
    return board

def main():
    sudoku_board = input_sudoku()

    print("\nOriginal Sudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Puzzle:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists")

if __name__ == "__main__":
    main()
