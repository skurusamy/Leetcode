def checkPermutations(st1,st2):
    if len(st1) != len(st2):
        return False
    for i in st1:
        if i not in st2:
            return False
    return True

def alternative(st1,st2):
    if(sorted(st1) == sorted(st2)):
        return True
    else:
        return False

st1 = "abc"
st2 = "cbad"
print(checkPermutations(st1,st2))
print(alternative(st1,st2))