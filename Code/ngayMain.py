#!/usr/bin/env python3
import os
from ngayBoard import *

board = Board()

while(1):
    os.system('clear')
    board.printBoard()
    printString = 'Player ' + str(board.counter + 1) + ' >>> '
    board.c = input(printString)
    if(board.counter == 0):
        board.jeuSud()
    if(board.counter == 1):
        board.jeuNord()
