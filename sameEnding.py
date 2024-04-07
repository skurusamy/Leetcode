string1 = "abcab"
count = [0]*26
result = 0
for i in range(len(string1)):
    count[ord(string1[i])-ord('a')] += 1
for i in range(len(count)):
    result += count[i] * (count[i]+1)//2
print(result)