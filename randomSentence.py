'''
Generate a random sentence of length N from a given text. Logic:

Randomly select a word
The next word will be the subsequent contagious word from the previously selected word. If the next word occurs multiple times in the sentence, select randomly.
Continue until length fulfill required length

'''
from collections import defaultdict
import random
text = "hello this is a flexport interview and this is a hello and that was cool"
n = 4
ans = ""
s_list = text.split(" ")
sentence_map = defaultdict(list)
for i in range(len(s_list)):
    sentence_map[s_list[i]].append(i)
idx = random.randrange(0, len(s_list))
while n > 0:  
    ans += s_list[idx] + " "
    print(idx, ans)
    idx = (idx+1) % len(s_list)
    if len(sentence_map[s_list[idx]]) > 1:
        r = random.randrange(0, len(sentence_map[s_list[idx]]))
        idx = sentence_map[s_list[idx]][r]
        
    n -= 1

print(ans)
print(s_list)

