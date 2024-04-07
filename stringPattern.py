def encode(str1):
    hash = {}
    ans = ""
    i = 0
    for i in range(len(str1)):
        if str1[i] not in hash:
            hash[str1[i]] = i + 1
        else:
            hash[str1[i]] += 1
    for j in str1:
        ans = ans + str(hash[j])
    return ans


str_list = ["abc", "xyz", "edu", "sssw", "lll"]
pattern = "eeed"
encoded_ans = encode(pattern)
for i in str_list:
    if encode(i) == encoded_ans:
        print(i)
