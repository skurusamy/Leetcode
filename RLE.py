def RunLengthEncoding(s):
    ans = ""
    if len(s) < 2:
        return s
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        if count > 1:
            ans += s[i] + str(count)
        else:
            ans += s[i]
        i += 1
    return ans



s = "aa"
print(RunLengthEncoding(s))