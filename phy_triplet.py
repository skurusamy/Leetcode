import math
def findTriplet(arr,n):
    maximum = max(arr)
    hash = [0] * (maximum+1)
    for i in range(n):
        hash[arr[i]] += 1
    print(hash)
    for i in range(len(arr)):
        if(hash[i]==0):
            continue
        for j in range(len(arr)):
            if(i == j and hash[i]==1) or hash[j]==0:
                continue
            val = int(math.sqrt(i*i + j*j))
            if((val*val) != (i*i + j*j)):
                continue
            if(val > maximum):
                continue
            if(hash[val]):
                return True
    return False

#main
'''
n = int(input("Enter the size: "))
arr=[]
for i in range(n):
    arr.append(int(input()))
'''
arr = [2,3,1,2,3,4,0]
print(findTriplet(arr,7))