from collections import defaultdict
words = ["cat", "dog", "taz", "god", "act"]
groupedWords = defaultdict(list)

'''
# Put all anagram words together in a dictionary
# where key is sorted word
for word in words:
    groupedWords["".join(sorted(word))].append(word)
print(groupedWords)
    # Print all anagrams together
for group in groupedWords.values():
    print(" ".join(group))
'''
for word in words:
    w = "".join(sorted(word))
    groupedWords[w].append(word)
print(groupedWords.values())

