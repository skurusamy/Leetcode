import heapq,math
h =[]
for i in range(10):
    heapq.heappush(h,i)
print(h)
while(len(h)  > 1):
    stone1 = heapq._heappop_max(h)
    stone2 = heapq._heappop_max(h)
    heapq.heappush(h,abs(stone1 - stone2))

print(h)