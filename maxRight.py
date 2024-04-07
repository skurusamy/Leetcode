A=[16,5,17,15,1]
temp = A[len(A)-1]
A[len(A)-1] =-1
for i in range(len(A)-2,-1,-1):
    if temp > A[i]:
        A[i] = temp
    else:
        temp = A[i]
print(A)

'''
temp=[]
for i in range(len(A)-1):
    A[i] = max(A[i+1:])
A[len(A)-1] = -1
print(A)
'''