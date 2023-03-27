import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [' ']*9

        self.create_board()
        
    def create_board(self):
        self.buttons = []
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text=' ', font=('Arial', 30), height=1, width=2,
                                   command=lambda row=row, col=col: self.on_button_click(row, col))
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = 3*row + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win() or self.check_draw():
                self.game_over()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]
        for line in lines:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return False

    def check_draw(self):
        return ' ' not in self.board

    def game_over(self):
        for button in self.buttons:
            button.config(state='disabled')
        if self.check_win():
            winner = 'X' if self.current_player == 'O' else 'O'
            tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        else:
            tk.messagebox.showinfo("Game Over", "It's a draw!")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
