def strCombi(lst, n ):
    ans = []
    if n == 0:
        return [[]]
    else:
        for i in range(len(lst)):
            m = lst[i]
            rem = lst[i+1:]
            for j in strCombi(rem,n-1):
                ans.append([m] + j)
    return ans


st = input("Enter string:")
n = int(input("Enter number: "))
print(strCombi(st, len(st)))