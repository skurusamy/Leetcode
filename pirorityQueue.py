from queue import PriorityQueue
l = [1,1,2,8,2,3,4]
p = PriorityQueue()
for i in l:
    p.put(i)
while (not p.empty()):   
    print(p.get())
