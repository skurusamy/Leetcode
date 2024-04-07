import math
def isPower(num):
    if num == 1:
        return True
    for i in range(2,int(math.sqrt(num)+1)):
        p = i
        while p <=num:
            p = p * i
            if p == num:
                return True
    return False



num = 1210
print(isPower(num))
