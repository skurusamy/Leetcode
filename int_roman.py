
num = int(input("Enter the number:"))
l = ["I","IV", "V", "IX","X","XL","L", "XC", "C", "CD", "D", "CM", "M"]
m = [1,4,5,9,10,40, 50, 90,100, 400, 500, 900, 1000]
i =12
while(num):
    quo = num // m[i]
    num = num % m[i]
    while(quo):
        print(l[i],end="")
        quo -= 1
    i -= 1


'''
Roman to int

import sys
s = "VI"
letter = ['M','D','C','L','X','V','I']
values = [1000,500,100,50,10,5,1]
lastVal = sys.maxsize
currentVal =0
ans = 0
for i in s:
            ind = letter.index(i)
            currentVal = values[ind]
            if currentVal > lastVal:
                currentVal = currentVal - lastVal
                ans = ans - lastVal
            #print(ans, lastVal, currentVal)
            ans += currentVal
            lastVal = currentVal
            currentVal = 0
print(ans)
'''