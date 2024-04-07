import math

flag = 0
num = int(input("Enter the number: "))
if num == 1:
    print("True")
for x in range(2, int(math.sqrt(num)) + 1):
    p = x
    while p <= num:
        p *= x
        if p == num:
            flag = 1
            break
if flag == 0:
    print("False")
else:
    print("True")
