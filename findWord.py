from collections import defaultdict
magazine = input("Enter the sentence in magazine: ").split()
note = input("Enter the sentence in note: ").split()
dic = defaultdict(int)
for i in magazine:
    dic[i] += 1
for i in note:
    if dic[i] == 0:
        print('No')
    else:
        dic[i] -= 1;
        print('Yes')