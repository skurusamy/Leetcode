from collections import defaultdict
words = ['cat','dog','rat', 'god']
dic = defaultdict(list)
for w in words:
    word="".join(sorted(w))
    dic[word].append(w)
print(dic.values())