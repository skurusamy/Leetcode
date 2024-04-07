columnNum = (int)(input("Enter the column Number: "))
columnName = [""]* 26
result =" "
i=0
while(columnNum >0 ):
    rem = columnNum % 26
    if rem == 0 :
        columnName[i] = 'Z'
        columnNum = columnNum // 26 -1
    else:
        columnName[i] = chr(rem -1 + 65)
        columnNum = columnNum // 26
    i += 1
columnName = columnName[::-1] #reverse
for j in columnName:
    result += j
print(result)
