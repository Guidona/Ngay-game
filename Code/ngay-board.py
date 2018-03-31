# class Board:
#     def __init__(self):
#         self.init()

#     def init(self):
#         self.cases = [
#             5,5,5,5,5,
#             5,5,5,5,5
#         ]
    
#     def printOnScreen(self):
#         count = 0
#         for i in self.cases
#             if(counter == 5)
#                 print "\n"
#             print i

counter = 1

cases = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
grenier = [0, 0, 0, 0, 0]

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