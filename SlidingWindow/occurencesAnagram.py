def isAnagram(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    return False

def countOccurrences(s1,s2):
    if len(s1) == 0 or len(s2) == 0:
        return 
    start = 0
    end = 0
    count = 0
    k = len(s2)
    while end < len(s1):
        if end - start + 1 < k:
            end += 1
        elif end - start + 1 == k:
            temp_s2 = s1[start:end+1]
            if isAnagram(temp_s2,s2):
                count+= 1
            start += 1
            end += 1
    return count

s1 = "foaxxorfraofrrrrfr"
s2 = "rfr"
print(countOccurrences(s1,s2))