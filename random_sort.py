import random
l = [4,2,5,6]
set_index = set()
'''
for i in range(len(l)):
    set_index.append(i) #[0,1,2,3]
while (set_index):
    i = random.randrange(0,len(set_index) )
    j = random.randrange(0, len(set_index) )
    ind1 , ind2 = set_index[i],set_index[j]
    if ind1 in set_index and ind2 in set_index and ind1 != ind2:
        set_index.remove(ind1)
        set_index.remove(ind2)
        temp = l[ind1]
        l[ind1] = l[ind2]
        l[ind2] = temp
print(l)
'''
while len(set_index) < len(l):
    i = random.randrange(0,len(l))
    if l[i] not in set_index:
        set_index.add(l[i])
print(set_index)