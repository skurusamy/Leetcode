# leetcode Qn . Reorder Data in Log Files
from posixpath import split


def reorderLogFiles(logs):
    letterLog = []
    digitLog = []
    for log in logs:
        temp =[]
        temp = log.split(" ")
        if temp[1].isalpha():
            letterLog.append(log)
        else:
            digitLog.append(log)
    
    return sorted(letterLog,key=lambda x:(x.split(" ",1)[1], x.split(" ",1)[0])) + digitLog


logs= ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))