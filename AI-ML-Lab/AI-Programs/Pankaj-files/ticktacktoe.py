def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  
            return True
        if all([board[j][i] == player for j in range(3)]):  
            return True
    if all([board[i][i] == player for i in range(3)]):  
        return True
    if all([board[i][2-i] == player for i in range(3)]):  
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def player_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2) separated by a space: ").split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken, choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column between 0 and 2.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        current_player = players[turn % 2]
        player_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1

if __name__ == "__main__":
    play_game()
