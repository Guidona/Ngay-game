#!/usr/bin/env python3
import os
from ngayBoard import *

board = Board()

while(1):
    # Clear the screen in order to have only a single game board in view
    os.system('cls' if os.name == 'nt' else 'clear')
    # Printing the game board
    board.printBoard()
    # Verifying if there isn't any deadlock in the game
    if(board.verifDeadlock() == True):
        print("Fin de la partie")
        break
    printString = 'Player ' + str(board.counter + 1) + ' >>> '
    board.c = input(printString)
    # Player ones game turn
    if(board.counter == 0):
        board.jeuSud()
    #Player twos game turn
    if(board.counter == 1):
        board.jeuNord()
