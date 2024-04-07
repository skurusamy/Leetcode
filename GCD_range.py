'''
GCDs of given index ranges in an array
Given an array a[0 . . . n-1]. 
We should be able to efficiently find the GCD from index qs (query start) to qe (query end) where 0 <= qs <= qe <= n-1.
'''

# gcd of two numbers
def gcd(a,b):
    if a==0 :
        return b
    if b ==0 :
        return a 
    if a == b :
        return a
    elif a > b:
        return gcd((a-b) ,b)
    else:
        return gcd((b-a) ,a)


arr = [2, 3, 60, 90, 50]  
qs= 0
qe = 2
gcdans = 0
for i in range(qs,qe+1):
    gcdans =   gcd(gcdans,arr[i])    
print(gcdans)