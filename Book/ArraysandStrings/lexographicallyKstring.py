'''
input: N = 3, K = 10 
Output: “aaj” 
Explanation: The 10th string in the lexicographical order starting from “aaa” is “aaj”.
Input: N = 2, K = 1000 
Output: -1 
Explanation: A total of 26*26 = 676 strings of length 2 are possible. So the output will be -1.

'''
n = 3
k =10
# condition checking
possibleAns = 26 ** 2
print(possibleAns)
if possibleAns >  k:
    k -= 1
    initialStringIndex = [0]*n
    for i in range(n-1,-1,-1):
        initialStringIndex[i] = k % 26
        k = k // 26
    for i in range(len(initialStringIndex)):
        initialStringIndex[i] = chr(initialStringIndex[i] + ord('a'))
    ans = ""
    for i in initialStringIndex:
        ans += i
    print(ans)
else:
    print("NOt possible")