class Exercise:
    def __init__(self, data):
        self.formatData(data)
    
    def formatData(self, data: str):
        self.reports = []
        for line in data.splitlines():
            report = line.split(' ')
            self.reports.append([int(level) for level in report])
            
    def solution(self):
        reportSafety = []
        for report in self.reports:
            status = ''
            res = False
            for i in range(len(report)):
                if i == len(report) - 1:
                    continue
                if status != '':
                    if status == 'in' and report[i] > report[i+1]:
                        res = False
                        break
                    if status == 'de' and report[i] < report[i+1]:
                        res = False
                        break
                difference = abs(report[i] - report[i+1])
                if difference < 1 or difference > 3:
                    res = False
                    break
                if report[i] > report[i+1] and status == '':
                    status = 'de'
                elif report[i] < report[i+1] and status == '':
                    status = 'in'
                res = True
            if res:
                reportSafety.append(True)
            else:
                reportSafety.append(False)
        return reportSafety.count(True)
    
    def checkOneBadLevel(self, index, report):
        modifiedReport = report[:]
        modifiedReport.pop(index)
        res = True
        status = ''
        for i in range(len(modifiedReport)):
            if i == len(modifiedReport) - 1:
                continue
            if status != '':
                if status == 'in' and modifiedReport[i] > modifiedReport[i+1]:
                    res = False
                    break
                if status == 'de' and modifiedReport[i] < modifiedReport[i+1]:
                    res = False
                    break
            difference = abs(modifiedReport[i] - modifiedReport[i+1])
            if difference < 1 or difference > 3:
                res = False
                break
            if modifiedReport[i] > modifiedReport[i+1] and status == '':
                status = 'de'
            elif modifiedReport[i] < modifiedReport[i+1] and status == '':
                status = 'in'
        return res
    
    def solution2(self):
        reportSafety = []
        for report in self.reports:
            status = ''
            badLevelCheck = False
            res = False
            for i in range(len(report)):
                if i == len(report) - 1:
                    break
                difference = report[i] - report[i+1]
                if status != '':
                    if status == 'in' and report[i] > report[i+1] and not badLevelCheck:
                        res = self.checkOneBadLevel(i+1, report)
                        pseudores = self.checkOneBadLevel(i, report)
                        if pseudores:
                            res = pseudores
                        pseudores = self.checkOneBadLevel(i-1, report)
                        if pseudores:
                            res = pseudores
                        badLevelCheck = True
                        break
                    if status == 'de' and report[i] < report[i+1] and not badLevelCheck:
                        res = self.checkOneBadLevel(i+1, report)
                        pseudores = self.checkOneBadLevel(i, report)
                        if pseudores:
                            res = pseudores
                        pseudores = self.checkOneBadLevel(i-1, report)
                        if pseudores:
                            res = pseudores
                        badLevelCheck = True
                        break 
                if abs(difference) < 1 or abs(difference) > 3 and not badLevelCheck:
                    res = self.checkOneBadLevel(i+1, report)
                    pseudores = self.checkOneBadLevel(i-1, report)
                    if pseudores:
                        res = pseudores
                    pseudores = self.checkOneBadLevel(i, report)
                    if pseudores:
                        res = pseudores
                    badLevelCheck = True
                    break
                if report[i] > report[i+1] and status == '':
                    status = 'de'
                elif report[i] < report[i+1] and status == '':
                    status = 'in'
                res = True
            if res:
                reportSafety.append(True)
            else:
                print(report)
                reportSafety.append(False)
        return reportSafety.count(True)