Arr = [-1,3,1,2,-4,-3]
for i in range(0,len(Arr)):
    l = i+1
    r = len(Arr) - 1
    x = Arr[i]
    while(l<r):
        if(x+Arr[l]+Arr[r] == 0):
            print(str(x)+" "+str(Arr[l])+" "+str(Arr[r]))
        if x+Arr[l]+Arr[r] > 0:
            r -= 1
        else:
            l+=1