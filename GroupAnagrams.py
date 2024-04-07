from collections import defaultdict

words = ["cat", "dog", "taz", "god", "act"]
groupedwords = defaultdict(list)
for word in words:
    ans = "".join(sorted(word,reverse=True))
    groupedwords[ans].append(word) 
print(groupedwords)


