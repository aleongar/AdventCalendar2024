class Exercise:
    def __init__(self, data):
        self.formatData(data)

    def formatData(self, data: str):
        max_length = max(len(row) for row in data.splitlines())
        self.data = [line.ljust(max_length) for line in data.splitlines()]

    def countViaSubstrSearch(self, string, line: str):
        return line.count(string)

    def countVertically(self):
        summatory = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows - 3): 
            for j in range(cols):
                if (self.data[i][j] == 'X' and self.data[i+1][j] == 'M' and
                    self.data[i+2][j] == 'A' and self.data[i+3][j] == 'S'):
                    summatory += 1
        return summatory

    def countVerticallyReverse(self):
        summatory = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows - 3): 
            for j in range(cols):
                if (self.data[i][j] == 'S' and self.data[i+1][j] == 'A' and
                    self.data[i+2][j] == 'M' and self.data[i+3][j] == 'X'):
                    summatory += 1
        return summatory

    def countDiagonalDownRight(self):
        summatory = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows - 3):
            for j in range(cols - 3): 
                if (self.data[i][j] == 'X' and self.data[i+1][j+1] == 'M' and
                    self.data[i+2][j+2] == 'A' and self.data[i+3][j+3] == 'S'):
                    summatory += 1
        return summatory

    def countDiagonalDownLeft(self):
        summatory = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows - 3): 
            for j in range(3, cols): 
                if (self.data[i][j] == 'X' and self.data[i+1][j-1] == 'M' and
                    self.data[i+2][j-2] == 'A' and self.data[i+3][j-3] == 'S'):
                    summatory += 1
        return summatory

    def countDiagonalDownRightReverse(self):
        summatory = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows - 3): 
            for j in range(cols - 3): 
                if (self.data[i][j] == 'S' and self.data[i+1][j+1] == 'A' and
                    self.data[i+2][j+2] == 'M' and self.data[i+3][j+3] == 'X'):
                    summatory += 1
        return summatory

    def countDiagonalDownLeftReverse(self):
        summatory = 0
        rows, cols = len(self.data), len(self.data[0])
        for i in range(rows - 3): 
            for j in range(3, cols):  
                if (self.data[i][j] == 'S' and self.data[i+1][j-1] == 'A' and
                    self.data[i+2][j-2] == 'M' and self.data[i+3][j-3] == 'X'):
                    summatory += 1
        return summatory

    def solution(self):
        summatory = 0
        for line in self.data:
            summatory += self.countViaSubstrSearch('XMAS', line)
            summatory += self.countViaSubstrSearch('SAMX', line)
        summatory += self.countVertically()
        summatory += self.countVerticallyReverse()
        summatory += self.countDiagonalDownRight()
        summatory += self.countDiagonalDownLeft()
        summatory += self.countDiagonalDownRightReverse()
        summatory += self.countDiagonalDownLeftReverse()
        return summatory

    def solution2(self):
        summatory = 0
        for i in range(len(self.data)-2):
            for j in range(len(self.data[i])-2):
                if self.data[i][j] == 'M' and self.data[i][j+2] == 'S' and self.data[i+1][j+1] == 'A' and self.data[i+2][j] == 'M' and self.data[i+2][j+2] == 'S':
                    summatory += 1
                    
        for i in range(len(self.data)-2):
            for j in range(len(self.data[i])-2):
                if self.data[i][j] == 'S' and self.data[i][j+2] == 'M' and self.data[i+1][j+1] == 'A' and self.data[i+2][j] == 'S' and self.data[i+2][j+2] == 'M':
                    summatory += 1
          
        for i in range(len(self.data)-2):
            for j in range(len(self.data[i])-2):
                if self.data[i][j] == 'M' and self.data[i][j+2] == 'M' and self.data[i+1][j+1] == 'A' and self.data[i+2][j] == 'S' and self.data[i+2][j+2] == 'S':
                    summatory += 1
                    
        for i in range(len(self.data)-2):
            for j in range(len(self.data[i])-2):
                if self.data[i][j] == 'S' and self.data[i][j+2] == 'S' and self.data[i+1][j+1] == 'A' and self.data[i+2][j] == 'M' and self.data[i+2][j+2] == 'M':
                    summatory += 1
        return summatory
