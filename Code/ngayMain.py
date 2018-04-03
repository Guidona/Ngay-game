#!/usr/bin/env python3
import os
from ngayBoard import *

board = Board()

while(1):
    os.system('cls' if os.name == 'nt' else 'clear')
    board.printBoard()
    printString = 'Player ' + str(board.counter + 1) + ' >>> '
    board.c = input(printString)
    if(board.counter == 0):
        board.jeuSud()
    if(board.counter == 1):
        board.jeuNord()
