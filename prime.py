import math
num = int(input("Enter a number: "))
ans =[1]
for val in range(2,num+1):
    for i in range(2,int(math.sqrt(val)+1)):
        if val % i == 0:
            break
    else:
        ans.append(val)
print(ans)