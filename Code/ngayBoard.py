class Board:
    def __init__(self):
        self.init()

    def init(self):
        self.c = ' '
        self.cases = [2, 0, 0, 2, 2, 2, 2, 2, 0, 2]
        self.counter = 0
        self.position = 0
        self.grenier = [0, 0]

    def gain(self):
        self.grenier[self.counter - 1] += self.cases[self.position - 1]
        self.cases[self.position - 1] = 0

    def incPosition(self):
        self.position += 1
        self.position %= 10

    def verifGain(self):
        count = 0
        if((self.cases[self.position - 1] == 2) or (self.cases[self.position - 1] == 4)):
            self.gain()
            count += 1
        self.incPosition()
        while(1):
            if((self.cases[self.position - 1] == 2) or (self.cases[self.position - 1] == 4)):
                self.gain()
                count += 1
            else:
                break
            if(self.position == 0 or self.position == 5):
                break
            self.incPosition()
        if(count == 1):
            print("Gain simple")
        if(count > 1):
            print("Gain cummulatif")

    def incCounter(self):
        self.counter += 1
        self.counter %= 2
            
    def jeuNord(self):
        if((self.c == '1') & (self.cases[9] > 1)):
            self.position = 0
            for i in range(0, self.cases[9]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[9] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == '2') & (self.cases[8] > 1)):
            self.position = 9
            for i in range(0, self.cases[8]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[8] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == '3') & (self.cases[7] > 1)):
            self.position = 8
            for i in range(0, self.cases[7]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[7] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == '4') & (self.cases[6] > 1)):
            self.position = 7
            for i in range(0, self.cases[6]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[6] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == '5') & (self.cases[5] > 1)):
            self.position = 6
            for i in range(0, self.cases[5]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[5] = 0
            self.incCounter()
            self.verifGain()
        else:
            self.counter = 1

    def jeuSud(self):
        if((self.c == 'A') & (self.cases[0] > 1)):
            self.position = 1
            for i in range(0, self.cases[0]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[0] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == 'B') & (self.cases[1] > 1)):
            self.position = 2
            for i in range(0, self.cases[1]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[1] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == 'C') & (self.cases[2] > 1)):
            self.position = 3
            for i in range(0, self.cases[2]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[2] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == 'D') & (self.cases[3] > 1)):
            self.position = 4
            for i in range(0, self.cases[3]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[3] = 0
            self.incCounter()
            self.verifGain()
        elif((self.c == 'E') & (self.cases[4] > 1)):
            self.position = 5
            for i in range(0, self.cases[4]):
                self.cases[self.position] += 1
                self.position += 1
                self.position = self.position % 10
            self.cases[4] = 0
            self.incCounter()
            self.verifGain()
        else:
            self.counter = 0

    def printBoard(self):
        print('')
        print('             ',self.grenier[1])
        print('')
        print('      1   2   3   4   5  ')
        print('    +---+---+---+---+---+')
        print('    |',self.cases[9],'|',self.cases[8],'|',self.cases[7],'|',self.cases[6],'|',self.cases[5],'|')
        print('    +---+---+---+---+---+')
        print('    |',self.cases[0],'|',self.cases[1],'|',self.cases[2],'|',self.cases[3],'|',self.cases[4],'|')
        print('    +---+---+---+---+---+')
        print('      A   B   C   D   E  ')
        print('')
        print('             ',self.grenier[0])
        print('')

