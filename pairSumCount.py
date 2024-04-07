'''
Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.
Input  :  arr[] = {1, 5, 7, -1}, 
          sum = 6
Output :  2
'''
arr = [1, 5, 7, -1]
sum =6 
countDic = {}
pairCount = 0
for i in arr:
    if i in countDic:
       countDic[i] += 1
    else:
        countDic[i] = 1
for i in arr:
    val = sum - i
    if val in countDic:
        pairCount += countDic[val]
    if val == i:
        pairCount -= 1
print(pairCount // 2)
