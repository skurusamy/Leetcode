def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


Arr = [1,2,3,4,5,6,7]
d=2
print(Arr)
itr = gcd(len(Arr),d)
for i in range(itr):
    temp=Arr[i]
    j = i
    while True:
        k = j + d
        if k >= len(Arr):
           k = k - len(Arr)
        if k == i:
            break
        Arr[j] = Arr[k]
        j = k
    Arr[j] = temp
print(Arr)

