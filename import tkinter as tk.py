import tkinter as tk
from tkinter import messagebox
import RoboConnect as RC

RC.RCC.greet()

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.playnumber = 0

        for i in range(3):
            for j in range(3):
                index = 3 * i + j
                button = tk.Button(
                    master,
                    text="",
                    font=("Helvetica", 60),
                    width=3,
                    height=1,
                    command=lambda idx=index: self.on_click(idx),
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            RC.RCC.PlaceElement(self, index)
            
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for combo in winning_combinations:
            if (
                self.board[combo[0]]
                == self.board[combo[1]]
                == self.board[combo[2]]
                != ""
            ):
                return True
        return False

    def check_draw(self):
        return all(cell != "" for cell in self.board)

    def reset_board(self):
        
        RC.RCC.ClearBoard(self)

        self.board = [""] * 9

        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()