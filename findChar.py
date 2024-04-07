from collections import defaultdict
st1 = input("Enter first string: ")
st2 = input("Enter second string: ")
dic = defaultdict(int)
for i in st1:
    dic[i] += 1
for i in st2:
    if dic[i] != 0:
        dic[i] -= 1
        print('Yes')
print('No')