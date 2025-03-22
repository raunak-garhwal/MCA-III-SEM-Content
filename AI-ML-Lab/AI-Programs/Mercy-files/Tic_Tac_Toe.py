def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6: print("--+---+--")

def check_winner(board, player):
    win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    return any(board[c[0]] == board[c[1]] == board[c[2]] == player for c in win_combos)

def is_draw(board): 
    return ' ' not in board

def tic_tac_toe():
    board, current_player = [' '] * 9, 'X'
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ' or not (0 <= move <= 8): raise ValueError
        except (ValueError, IndexError):
            print("Invalid move. Try again.")
            continue
        
        board[move] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
