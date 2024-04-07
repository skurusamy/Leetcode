columnName = input("Enter the column name ")
columnNum = 0
times = len(columnName) - 1
for i in range(len(columnName)):
    columnNum += ((ord(columnName[i]) - ord('A')) + 1 ) * ( 26 ** times)
    times -= 1
print(columnNum)