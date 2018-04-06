class Board:
    def __init__(self):
        self.init()

    def init(self):
        self.c = ' '
        self.cases = [1, 0, 0, 1, 2, 1, 1, 1, 0, 1]
        self.counter = 0
        self.position = 0
        self.grenier = [0, 0]

    def gain(self):
        self.grenier[self.counter - 1] += self.cases[self.position - 1]
        self.cases[self.position - 1] = 0

    def incPosition(self):
        self.position += 1
        self.position %= 10

    # Gain verification
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

    # Counter incrementer
    def incCounter(self):
        self.counter += 1
        self.counter %= 2
            
    # Utility function for distribution
    def distribution(self, boardPosition, boardCase):
        self.position = boardPosition
        for i in range(0, self.cases[boardCase]):
            self.cases[self.position] += 1
            self.position += 1
            self.position = self.position % 10
        self.cases[boardCase] = 0
        self.incCounter()
        self.verifGain()

    # Player twos game
    def jeuNord(self):
        if((self.c == '1') & (self.cases[9] > 1)):
            self.distribution(0, 9)
        elif((self.c == '2') & (self.cases[8] > 1)):
            self.distribution(9, 8)
        elif((self.c == '3') & (self.cases[7] > 1)):
            self.distribution(8, 7)
        elif((self.c == '4') & (self.cases[6] > 1)):
            self.distribution(7, 6)
        elif((self.c == '5') & (self.cases[5] > 1)):
            self.distribution(6, 5)
        else:
            self.counter = 1

    # Player ones game
    def jeuSud(self):
        if((self.c == 'A') & (self.cases[0] > 1)):
            self.distribution(1, 0)
        elif((self.c == 'B') & (self.cases[1] > 1)):
            self.distribution(2, 1)
        elif((self.c == 'C') & (self.cases[2] > 1)):
            self.distribution(3, 2)
        elif((self.c == 'D') & (self.cases[3] > 1)):
            self.distribution(4, 3)
        elif((self.c == 'E') & (self.cases[4] > 1)):
            self.distribution(5, 4)
        else:
            self.counter = 0

    # verifDeadlock function to verify if there isn't any dead lock in the game in order to stop
    def verifDeadlock(self):
        for i in self.cases:
            if i > 1:
                return False
        return True

    # Function to print the board to the screen
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

