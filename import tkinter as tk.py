import tkinter as tk
from tkinter import messagebox
import numpy
import math
import time


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
            
            RoboConnect.PlaceElement(self, index)
            
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
        
        RoboConnect.ClearBoard(self)

        self.board = [""] * 9

        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

class RoboConnect:
    def __init__(self):

        self.current_player = "X"
        self.board = [""] * 9
        self.playnumber = 0

    def greet():
        print("RoboConnect linked and ready")
        Locations.greet()
        return

    def dataparse(self, index):
        self.board
        self.current_player
        

        print(self.board) #current Board
        print(self.current_player) #current Player
        print(index) #index of the latest play

        return

    def ClearBoard(self):
        player = "X"
        #board = []
        board = self.board

        playnumber = self.playnumber

        for i in range(playnumber):
        
            index_retreive = board.index(player)

            retreive_location = Locations.NGLocationData(index_retreive)
            play_location = Locations.OGLocationData(i)

            print(retreive_location)
            print(play_location)

            #Robot.pickup(retreive_location)
            #Robot.place(play_location)

            if (player == "X"):
                player = "O"
            else:
                player = "X"

            print(board)
            board[index_retreive] = ""
            print(board)
            print()

        print("Board Cleared")
        self.playnumber = 0
        return
    
    def PlaceElement(self, index):
        print("Getting locations")
        retreive_location = Locations.OGLocationData(self.playnumber)
        play_location = Locations.NGLocationData(index)

        print("sending to robot")
        #print(self.current_player) #current Player
        #print(index) #index of the latest play
        print(retreive_location)
        print(play_location)
        #print(self.playnumber)

        #Robot.pickup(retreive_location)
        #Robot.place(play_location)
        
        self.playnumber = self.playnumber + 1

        return
    
class Locations:

    elementgrid = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

    def greet():
        print("Layout linked and ready")
        return

    def NGLocationData(index):
        boardX = 0.0
        boardY = 0.0

        GridElementOffset = 66.0 #in mm

        GridOffsetX = 152.5 #in mm
        GridOffsetY = 462.5 #in mm

        index = index

        position = []

        #X Position
        if(index in [0, 3, 6]):
            X = GridOffsetX - GridElementOffset

        elif(index in [1, 4, 7]):
            X = GridOffsetX

        elif(index in [2, 5, 8]):
            X = GridOffsetX + GridElementOffset  

        #Y Position
        if(index in [0, 1, 2]):
            Y = GridOffsetY + GridElementOffset

        elif(index in [3, 4, 5]):
            Y = GridOffsetY

        elif(index in [6, 7, 8]):
            Y = GridOffsetY - GridElementOffset

        position = [X, Y]

        return(position)
    
    def OGLocationData(index):
        boardX = 0.0
        boardY = 0.0

        GridElementOffset = 66.0 #in mm

        GridOffsetX = -152.5 #in mm
        GridOffsetY = 462.5 #in mm

        index = index

        position = []

        #X Position
        if(index in [0, 3, 6]):
            X = GridOffsetX - GridElementOffset

        elif(index in [1, 4, 7]):
            X = GridOffsetX

        elif(index in [2, 5, 8]):
            X = GridOffsetX + GridElementOffset  

        #Y Position
        if(index in [0, 1, 2]):
            Y = GridOffsetY + GridElementOffset

        elif(index in [3, 4, 5]):
            Y = GridOffsetY

        elif(index in [6, 7, 8]):
            Y = GridOffsetY - GridElementOffset

        position = [X, Y]

        return(position)

    def resetLocation():

        elementgrid = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

class Robot:

    def greet():
        print("Hello")

    def pickup(Location_Data):
        #going to pickup loaction
        #go to xy
        #go down in Z
        #grab object
        #Go up in Z
        
        return
    
    def place(Location_Data): 
        #going to place location
        #go to xy
        #go down in Z
        #release object
        #Go up in Z
        #go to neutral spot
        
        return
           
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()