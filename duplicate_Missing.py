n = int(input("Enter array size: "))
arr = []
for i in range(n):
    arr.append(int(input()))
hash = {}
'''
for i in range(n):
    if arr[abs(arr[i]) - 1] > 0:
        arr[abs(arr[i]) -1] = - arr[abs(arr[i]) -1]
    else:
        print(abs(arr[i]))
print(arr)
for i in range(n):
    if arr[i] < 0 :
        continue;
    else:
        print("Missing: "+ str(i+1))
'''
print("Duplicate:",end=" ")
for i in arr:
    if(hash.get(i)== None):
        hash[i] = True
    else:
        print(i)
print(hash)
print("\nMissing: ",end=" ")
for i in range(n):
    if(hash.get(i+1)==None):
        print(i+1)
