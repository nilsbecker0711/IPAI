class Board:
    def init(self):
        self.gameboard = [['(0,0)','(0,1)', '(0,2)'], ['(1,0)', '(1,1)', '(1,2)'],['(2,0)','(2,1)', '(2,2)']]
        self.printBoard()

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                if j == 2:
                    print(' ' + self.gameboard[i][j])
                else:
                    print(' ' + self.gameboard[i][j],'|', end = '')

b = Board()
b.init()
