def permutations(st1):
    ans =[]
    permutationHelper("",st1,ans)
    return ans

def permutationHelper(helper,st1,ans):
    if len(st1) == 0:
        ans.append(helper+st1)
        return
    for i in range(len(st1)):
        permutationHelper(helper+st1[i],st1[0:i]+st1[i+1:len(st1)],ans)
st1 = "abc"
print(permutations(st1))