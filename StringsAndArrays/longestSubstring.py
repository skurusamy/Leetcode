def longestSubStringWithoutRepeatingCharacters(st):
    if st is None:
        return
    a_pointer = 0
    b_pointer = 0
    temp = []
    ans_str = ""
    ans = -9099787
    while b_pointer < len(st):
        if st[b_pointer] not in temp:
            temp.append(st[b_pointer])
            b_pointer += 1
        else:
            if ans <  len(temp):
                ans = len(temp)
                ans_str = st[a_pointer:b_pointer]
            a_pointer = b_pointer
            temp =[]
    return ans_str


s = "pwwkew"
print(longestSubStringWithoutRepeatingCharacters(s))