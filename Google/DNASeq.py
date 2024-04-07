'''
Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
'''
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
L = 10
i = 0
hash ={}
output = []
while (i + 10) < len(s):
    temp = s[i:i+10]
    if temp not in hash:
        hash[temp] = 1
    else:
        hash[temp] += 1
    if hash[temp] == 2:
        output.append(temp)
    i += 1
print(hash)
print(output)