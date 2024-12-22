class Exercise:
    def __init__(self, data):
        self.formatData(data)
        self.leftColumn.sort()
        self.rightColumn.sort()
        
    def formatData(self, data: str):
        transformed_Data = data.splitlines()
        self.leftColumn = []
        self.rightColumn = []
        for line in transformed_Data:
            splr = line.split('   ')
            self.leftColumn.append(int(splr[0]))
            self.rightColumn.append(int(splr[1]))
    
    def solution(self):
        distances = []
        for i in range(len(self.leftColumn)):
            left_val = self.leftColumn.pop(0)
            right_val = self.rightColumn.pop(0)
            distances.append(abs(left_val - right_val))
        return sum(distances)
    
    def solution2(self):
        scores = []
        for i in range(len(self.leftColumn)):
            left_val = self.leftColumn[i]
            quantity = self.rightColumn.count(left_val)
            scores.append(left_val * quantity)
        return sum(scores)