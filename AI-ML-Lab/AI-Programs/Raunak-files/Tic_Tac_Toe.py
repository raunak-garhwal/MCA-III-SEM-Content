import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' '] * 9
        self.user = ''
        self.computer = ''
        self.buttons = []
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.master, text=' ', font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def start_game(self):
        self.user = ''
        while self.user not in ['X', 'O']:
            self.user = messagebox.askquestion("Choose your symbol", "Do you want to be X?") == 'yes'
            self.user = 'X' if self.user else 'O'
        self.computer = 'O' if self.user == 'X' else 'X'
        self.update_board()

    def update_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i])

    def player_move(self, move):
        if self.board[move] == ' ':
            self.board[move] = self.user
            self.update_board()
            if self.check_winner(self.user):
                self.master.after(1000, lambda: self.show_winner(self.user))
                return
            if self.is_draw():
                self.master.after(1000, self.show_draw)
                return
            self.master.after(1000, self.computer_move)

    def computer_move(self):
        move = self.get_best_move(self.board, self.computer, self.user)
        self.board[move] = self.computer
        self.update_board()
        if self.check_winner(self.computer):
            self.master.after(1000, lambda: self.show_winner(self.computer))
            return
        if self.is_draw():
            self.master.after(1000, self.show_draw)

    def show_winner(self, winner):
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_game()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.board = [' '] * 9
        self.update_board()
        self.start_game()

    def check_winner(self, player):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(self.board[c[0]] == self.board[c[1]] == self.board[c[2]] == player for c in win_combos)

    def is_draw(self):
        return ' ' not in self.board

    def get_best_move(self, board, player, opponent):
        # Winning Move
        for move in range(9):
            if board[move] == ' ':
                board[move] = player
                if self.check_winner(player):
                    return move
                board[move] = ' '

        # Blocking Move
        for move in range(9):
            if board[move] == ' ':
                board[move] = opponent
                if self.check_winner(opponent):
                    return move
                board[move] = ' '

        # Center move
        if board[4] == ' ':
            return 4

        # Take a corner if available
        for move in [0, 2, 6, 8]:
            if board[move] == ' ':
                return move

        # Take any remaining move
        return random.choice([i for i in range(9) if board[i] == ' '])

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
