"""
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Output: 3
"""

n = int(input("Enter the number of socks: "))
arr = []
dic = {}
count = 0
print("Enter the socks numbers: ")
for i in range(n):
    arr.append(int(input()))
for i in arr:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] = dic[i]+1
print(dic)
for i in dic.keys():
    count += dic[i]//2

print("The number of individual socks are", count)