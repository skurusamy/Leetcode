'''
input = TactCoa
output = True [ Permutation:"taco cat"]
'''
def palindromePermutation(st):
    result = []
    for i in st:
        if i == ' ':
            pass
        elif i not in result:
            result.append(i)
        else:
            result.remove(i)
    #print(result)
    if len(result) == 0 or len(result) == 1:
        return True
    else:
        return False

st = "Tact Coac"
print(palindromePermutation(st.lower()))