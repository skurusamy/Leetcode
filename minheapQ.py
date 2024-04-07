import heapq;
li = [3,45,56,7,30,2,88,9]
print("Heapify: ")
heapq.heapify(li)
print(li)
heapq.heappush(li,20);
print("Heapify: ")
heapq.heapify(li)
print(li)

print(heapq.nlargest(3,li))
print(heapq.nsmallest(4,li))