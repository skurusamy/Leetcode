'''
Find the first non-repeating element in a given array of integers.
Input : -1 2 -1 3 2
Output : 3
Explanation : The first number that does not 
repeat is : 3
'''

arr =[-1,2,-1,4,3,2,3]
dic ={}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
for i in dic.keys():
    if dic[i] == 1:
        print(i)
        break