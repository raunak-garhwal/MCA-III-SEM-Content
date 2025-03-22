def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def solveNQUtil(board, col):
    if col >= N:
        return True

    for i in range(N):
        if ((ld[i - col + N - 1] != 1) and (rd[i + col] != 1) and (cl[i] != 1)):
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if solveNQUtil(board, col + 1):
                return True

            board[i][col] = 0
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

    return False

def solveNQ():
    board = [[0 for _ in range(N)] for _ in range(N)]
    global ld, rd, cl
    ld = [0] * (2 * N - 1)
    rd = [0] * (2 * N - 1)
    cl = [0] * N

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

N = int(input("Enter the value of N: "))
solveNQ()
