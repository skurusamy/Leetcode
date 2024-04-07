'''
input:
cde
abc
outpput:
4
Delete the following characters from the strings make them anagrams:
Remove d and e from cde to get c.
Remove a and b from abc to get c.

4 deletion

'''

from collections import  defaultdict
s1 = input("Enter string1:")
s2 = input("Enter string2:")
sum =0
dic =defaultdict(int)
for i in s1:
    dic[i] = dic[i]+1
for i in s2:
    dic[i] = dic[i] - 1
for i in dic.keys():
    sum +=  abs(dic[i])
print(sum)
