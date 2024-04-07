import  sys
arr = [1,8,6,2,5,4,8,3,7]
maxi = -sys.maxsize
"""
for i in range(len(arr)):
    for  j in range(i+1,len(arr)):
        mini = min(arr[i],arr[j])
        maxi = max(maxi,mini *(j-i))
print(maxi)
"""
i = 0 
j =len(arr)-1
while(i<j):
    mini = min(arr[i],arr[j])
    maxi = max(maxi,mini*(j-i))
    if(arr[i]<arr[j]):
        i += 1
    else:
        j -=1
print(maxi)