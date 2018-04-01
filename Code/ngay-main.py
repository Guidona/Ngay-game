#!/usr/bin/env python3
import os

counter = 0
position = 0

cases = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
grenier = [0, 0]
maisons = ["A","B","C","D","E","5","4","3","2","1"]

def verifGain(counter, position):
    if((cases[position - 1] == 2) or (cases[position - 1] == 4)):
        grenier[counter] += cases[position - 1]
        cases[position - 1] = 0
        print("gain simple")
        
def verifPosition(position):
    return position % 10

def incCounter(counter):
    counter += 1
    return counter % 2
        
def jeuNord(c):
    if((c == '1') & (cases[9] > 1)):
        position = 0
        for i in range(0, cases[9]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[9] = 0
    if((c == '2') & (cases[8] > 1)):
        position = 9
        for i in range(0, cases[8]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[8] = 0
    if((c == '3') & (cases[7] > 1)):
        position = 8
        for i in range(0, cases[7]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[7] = 0
    if((c == '4') & (cases[6] > 1)):
        position = 7
        for i in range(0, cases[6]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[6] = 0
    if((c == '5') & (cases[5] > 1)):
        position = 6
        for i in range(0, cases[5]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[5] = 0
    verifGain(counter, position)

def jeuSud(c):
    if((c == 'A') & (cases[0] > 1)):
        position = 1
        for i in range(0, cases[0]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[0] = 0
    if((c == 'B') & (cases[1] > 1)):
        position = 2
        for i in range(0, cases[1]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[1] = 0
    if((c == 'C') & (cases[2] > 1)):
        position = 3
        for i in range(0, cases[2]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[2] = 0
    if((c == 'D') & (cases[3] > 1)):
        position = 4
        for i in range(0, cases[3]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[3] = 0
    if((c == 'E') & (cases[4] > 1)):
        position = 5
        for i in range(0, cases[4]):
            cases[position] += 1
            position += 1
            position = position % 10
        cases[4] = 0
    verifGain(counter, position)

def printBoard():
    print('')
    print('             ',grenier[1])
    print('')
    print('      1   2   3   4   5  ')
    print('    +---+---+---+---+---+')
    print('    |',cases[9],'|',cases[8],'|',cases[7],'|',cases[6],'|',cases[5],'|')
    print('    +---+---+---+---+---+')
    print('    |',cases[0],'|',cases[1],'|',cases[2],'|',cases[3],'|',cases[4],'|')
    print('    +---+---+---+---+---+')
    print('      A   B   C   D   E  ')
    print('')
    print('             ',grenier[0])
    print('')

while(1):
    printBoard()
    printString = 'player' + str(counter + 1) + ' >>> '
    c = input(printString)
    if(counter == 0):
        jeuNord(c)
    if(counter == 1):
        jeuSud(c)
    counter = incCounter(counter)
