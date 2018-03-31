#!/usr/bin/env python3
import os

counter = 1
position = 0

cases = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
grenier = [0, 0, 0, 0, 0]
maisons = ["A","B","C","D","E","F","G","H","I","J"]

def verifGain(counter, position):
    if((cases[position - 1] == 2) or (cases[position - 1] == 4)):
        grenier[counter] += cases[position - 1]
        cases[position - 1] = 0
        print("gain simple")
        
def verifPosition(position):
    if(position > 9):
        position = 0
    return position

def incCounter(counter):
    counter += 1
    if(counter > 5):
        counter = 1
        
def printBoard():
    print('')
    print('           ',grenier[4],'     ',grenier[3])
    print('')
    print('      J   I   H   G   F  ')
    print('    +---+---+---+---+---+')
    print('    |',cases[9],'|',cases[8],'|',cases[7],'|',cases[6],'|',cases[5],'|')
    print(grenier[0],'  +---+---+---+---+---+')
    print('    |',cases[0],'|',cases[1],'|',cases[2],'|',cases[3],'|',cases[4],'|')
    print('    +---+---+---+---+---+')
    print('      A   B   C   D   E  ')
    print('')
    print('           ',grenier[1],'     ',grenier[2])
    print('')

while(1):
    printBoard()
    printString = 'player' + str(counter) + ' >>> '
    c = input(printString)
    if(counter == 1):
        # if((c == 'A') or (c == 'J')):
        if((c == 'J') & (cases[9] > 1)):
            poing = cases[9]
            position = 0
            cases[9] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        if((c == 'A') & (cases[0] > 1)):
            poing = cases[0]
            position = 1
            cases[0] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        verifGain(0, position)
    elif(counter == 2):
        # if((c == 'B') or (c == 'C')):
        if((c == 'B') & (cases[1] > 1)):
            poing = cases[1]
            position = 2
            cases[1] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        if((c == 'C') & (cases[2] > 1)):
            poing = cases[2]
            position = 3
            cases[2] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        verifGain(1, position)
    elif(counter == 3):
        # if((c == 'D') or (c == 'E')):
        if((c == 'D') & (cases[3] > 1)):
            poing = cases[3]
            position = 4
            cases[3] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        if((c == 'E') & (cases[4] > 1)):
            poing = cases[4]
            position = 5
            cases[4] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        verifGain(2, position)
    elif(counter == 4):
        # if((c == 'F') or (c == 'G')):
        if((c == 'F') & (cases[5] > 1)):
            poing = cases[5]
            position = 6
            cases[5] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        if((c == 'G') & (cases[6] > 1)):
            poing = cases[6]
            position = 7
            cases[6] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        verifGain(3, position)
    else:
        # if((c == 'H') or (c == 'I')):
        if((c == 'H') & (cases[7] > 1)):
            poing = cases[7]
            position = 8
            cases[7] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        if((c == 'I') & (cases[8] > 1)):
            poing = cases[8]
            position = 9
            cases[8] = 0
            for i in range(0, poing):
                cases[position] += 1
                position += 1
                position = verifPosition(position)
        verifGain(4, position)
    counter += 1
    if(counter > 5):
        counter = 1
