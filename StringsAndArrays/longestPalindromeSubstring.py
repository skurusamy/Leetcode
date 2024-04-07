'''
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

'''
def longestPalindromeSubstringCount(s,r):
    ans = ""
    dp = [[-1 for _ in range(len(r))] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(r)):
            if i == 0 or j == 0:
                dp[i][j] = 0
    for i in range(1, len(s)):
        for j in range(1, len(r)):
            if s[i] != r[j]:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            else:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans += s[i]
    
    return dp[i][j]    

# Expand From center
def expandFromCenter(s, left, right):
    if s is None or left > right :
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
def longestPalindromeSubstring(s):
    if s is None:
        return ""
    left = 0
    end = 0
    for i in range(len(s)):
        len1 = expandFromCenter(s, i, i) # abba
        len2 = expandFromCenter(s, i, i+1) #racecar
        ans = max(len1, len2)
        if ans > end - left: # some palindrome is found
            left = i - ((ans -1) //2)
            end = i + (ans//2)
    return s[left:end+1]

s = "babad"
r = s[::-1]
#print(longestPalindromeSubstringCount(s,r))
print(longestPalindromeSubstring(s))


