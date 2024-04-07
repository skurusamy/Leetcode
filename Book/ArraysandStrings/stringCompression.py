def stringCompression(st):
    st = list(st)
    ans  = []
    i = 0
    while i<len(st):
        j = i
        while j < len(st) and st[j] == st[i] :
            j += 1
        if j - i >= 1:
            ans.append(st[i])
            ans.append(str(j-i))  
        i = j
    return ans
st = "aabccccb"
print(stringCompression(st))