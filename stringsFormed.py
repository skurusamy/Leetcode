def stringOc(n,bcount,c):
    res = 0
    if bcount < 0 or c < 0:
        return 0
    if n == 0:
        return 1
    if bcount == 0  and c ==0:
        return 1

    res = stringOc(n-1,bcount,c)
    res += stringOc(n-1,bcount-1,c)
    res += stringOc(n-1,bcount,c-1)
    return  res
n = int(input("Enter n: "))
print(stringOc(n,1,2))