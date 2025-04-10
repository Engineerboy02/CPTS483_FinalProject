import numpy
import math
import time


class RCC:
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
            #Robot.place(retreive_location)

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

    def pickup(location):

        return
    def place(location):

        return