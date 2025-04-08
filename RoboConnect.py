import numpy
import math
import time


class RCC:
    def __init__(self):

        self.current_player = "X"
        self.board = [""] * 9
        

    def greet():
        print("RoboConnect linked and ready")
        Location.greet()
        return

    def dataparse(self, index):
        self.board
        self.current_player
        

        print(self.board) #current Board
        print(self.current_player) #current Player
        print(index) #index of the latest play

        return

    def ClearBoard(self):
        print("Board Cleared")
        return
    
    def PlaceElement(self, index):
        print("Getting location")
        play_location = Location.NGLocationData(index)

        print("sending to robot")
        print(self.current_player) #current Player
        print(index) #index of the latest play
        print(play_location)
        
        #Robot.pickup(self.current_player)
        #Robot.place(play_location)
        
        

        return
    
class Location:
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