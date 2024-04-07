
def hasDuplicates(arr):
    hash = {}
    for i in arr:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    for i in hash.values():
        if i != 1:
            return True
    return False


arr = [1,2,3,4]
print(hasDuplicates(arr))