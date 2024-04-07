'''
Given an array of size n and a number k, find all elements that appear more than n/k times
'''
arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
ans = set()
occurrence = len(arr) // k
dic ={}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in dic.keys():
    if dic[i] > occurrence:
        ans.add(i)
print(ans)