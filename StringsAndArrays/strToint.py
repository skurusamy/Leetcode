'''
Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.



Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

'''

def strToInt(s):
    ans = "0"
    if s is None:
        return
    isNegative = (s[0] == '-')
    print(isNegative)
    for i in range(len(s)):
        if s[i].isdigit():
            ans += s[i]
    if int(ans) > (2 ** 31) -1 :
        return (2**31) -1
    if int(ans) < -(2 ** 31) :
        return -(2 ** 31)
    if isNegative:
        return -1 * int(ans)
    else:
        return int(ans)
s = "-56567 words"
print(strToInt(s))

