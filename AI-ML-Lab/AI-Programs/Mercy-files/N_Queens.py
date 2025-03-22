def print_solution(board):
    print("\n".join(" ".join("Q" if col else "." for col in row) for row in board), "\n")

def is_safe(board, row, col, n):
    return all(board[i][col] == 0 and
               all(board[i][j] == 0 for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1))) and
               all(board[i][j] == 0 for i, j in zip(range(row-1, -1, -1), range(col+1, n)))
               for i in range(row))

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    if solutions:
        print(f"Total solutions: {len(solutions)}")
        for solution in solutions: print_solution(solution)
    else: print("No solution exists.")

def get_input():
    n = int(input("Enter the size of the chessboard (N): "))
    if n >= 4: n_queens(n)
    else: print("No solution exists for N < 4.")

get_input()
