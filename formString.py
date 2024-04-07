def formString(s1,s2):
    SubString = 0
    remaining = s2
    while(remaining):
        subseq = []
        i =0
        j =0
        while i< len(s1) and j < len(remaining):
            if s1[i] == remaining[j]:
                subseq.append(remaining[j])
                j += 1    
            i += 1  
        if len(subseq) == 0:
            return -1
        SubString += 1
        remaining = remaining[j:]
    return SubString
    


s1 = "xyz"
s2 ="xyxyxz"
print(formString(s1,s2))