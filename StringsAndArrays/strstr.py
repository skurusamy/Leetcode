def strStr(haystack,needle):
    if len(needle) == 0 :
            return 0
    if len(haystack) == 0 or len(haystack) < len(needle):
            return -1
    idx = -1
    j = 0
    for i in range(len(haystack)):
        if haystack[i] != needle[j]:
            i += 1
        else:
            idx = i
            i += 1
            j += 1
            while j < len(needle) and i < len(haystack):
                if haystack[i] != needle[j]:
                    i = idx
                    idx = -1
                    j = 0
                    break
                i += 1
                j += 1
            if j == len(needle):
                return idx
    return -1

haystack = "mississippi"
needle = "issipi"
print(strStr(haystack,needle))