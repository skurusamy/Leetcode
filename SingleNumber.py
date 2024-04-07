'''
In a non-empty array, every element appears thrice expect for one element find that one
'''

#arr = [2,2,3,2]
arr = [0,1,0,1,0,1,99]
dic ={}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in dic.keys():
    if(dic[i]==1):
        print(i)