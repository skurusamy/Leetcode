def strStr( haystack: str, needle: str) -> int:
        if len(needle) == 0 and len(haystack) == 0 :
            return 0
        
        if len(haystack) == 0:
            return -1
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                index = i
                k = i
                for j in range(len(needle)):
                    if k < len(haystack) and haystack[k] != needle[j]  :
                        break
                    k += 1
                if k > len(haystack):
                    return -1
                if j +1 == len(needle):
                    return index
        return -1
print(strStr("aaab","ab"))