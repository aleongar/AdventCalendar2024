import re
class Exercise:
    def __init__(self, data):
        self.formatData(data)
    
    def formatData(self, data):
        self.data = data
        
    def solution(self):
        patron = r"mul\(\d{1,3},\d{1,3}\)"
        results = re.findall(patron, self.data)
        sumatory = 0
        for result in results:
            if(result is None):
                continue
            vals = result.replace('mul(', '').replace(')','').split(',')
            sumatory += (int(vals[0]) * int(vals[1]))
        return sumatory
    
    def solution2(self):
        patron = r"mul\(\d{1,3},\d{1,3}\)"
        splitted = self.data.split('don\'t()')
        correctData = [splitted.pop(0)]
        for substr in splitted:
            datappend = substr.split('do()')
            datappend.pop(0)
            for dApp in datappend:
                correctData.append(dApp)
        results = []
        for cData in correctData:
            transform = re.findall(patron, cData)
            for match in transform:
                results.append(match)
        sumatory = 0
        for result in results:
            if result is None:
                continue
            vals = result.replace('mul(', '').replace(')','').split(',')
            sumatory += (int(vals[0]) * int(vals[1]))
        return sumatory