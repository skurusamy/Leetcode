"""
Given two sorted array find the median of two array in O(log(m,n)) time complexity
**********************************************************************************
Case 1:
    Brute Force technique:
        Merge 2 arraya and find the middle element
        Time and Space = O(n+m)
Case 2: Using binary search
        Find a partition in two array using binary search such that the elements on 
        left side is less than all elements on the right side
             median = avg(max(2left elements), min(2 right elements)) if even
             median = max(2 left elements) if odd
    Steps:
        Partition1 = (start1 + end1 )//2
        Partition2 = (len(1) + len(2) + 1) //2 - partition1
        Some conditions
"""
ASize = int(input("Enter the size of first Array: "))
firstArray = []
print("Enter Array Elements: ")
for i in range(ASize):
    firstArray.append(int(input()))
BSize = int(input("Enter the size of second Array: "))
secondArray = []
print("Enter the Array Elements: ")
for i in range(BSize):
    secondArray.append(int(input()))
median =0
start = 0
end = ASize
while start < end:
    partition1 = (start + end) // 2
    partition2 = (ASize + BSize + 1)//2 - partition1
    #if left of first array is greater --
    if(firstArray[partition1-1] > secondArray[partition2]) and (partition2< BSize and partition1 > 0):
        start -= 1
    #if left of second array is greater ++
    elif(firstArray[partition1] < secondArray[partition2-1]) and (partition2 > 0 and partition1 < ASize):
        start += 1
    else:
        if partition1 ==0:
            median = secondArray[partition2-1]
        elif partition2== 0 :
            median = firstArray[partition1-1]
        else:
            median = max(firstArray[partition1-1],secondArray[partition2]-1)
        break
if (ASize + BSize % 2 ==1):
    print(median)
if partition1 == ASize:
    print((median + secondArray[partition2])/2)
if partition2 == BSize:
    print((median+firstArray[partition1])/2)
else:
    print((median + min(firstArray[partition1],secondArray[partition2]))/2)