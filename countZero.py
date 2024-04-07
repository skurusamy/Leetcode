def countZero(Arr,start,end):
    if end> start:
        mid = (start+end)//2
        if(Arr[mid] ==0 and Arr[mid+ 1]==1) or mid == end:
            return mid+1
        if(Arr[mid] == 0 ):
            return countZero(Arr,mid+1,end)
        return countZero(Arr,start,mid-1)

Arr = [0,0,0,0,0,0,0,1,1,1,1,1]
print(countZero(Arr, 0,len(Arr)))