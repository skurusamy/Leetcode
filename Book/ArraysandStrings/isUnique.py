def isUnique(st):
    dic = {}
    for i in st:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic.keys():
        if dic[i] != 1:
            return False
    
    return True

st = "abc"
print(isUnique(st))