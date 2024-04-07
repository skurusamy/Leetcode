"""
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
The player must avoid the thunderheads
Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.
It is always possible to win the game.
7
0 0 1 0 0 1 0

Output: 4
"""

"""


n = int(input("Enter n:"))
arr =[]
count=0
for i in range(n):
    arr.append(int(input()))
i = 0
while i < len(arr)-1:
    if(arr[i] == 0):
        i += 1
    i += 1
    count += 1
print(count)
"""

def jumpingFrog(arr):
   if len(arr)==1:
       return 0
   if len(arr) == 2:
       if arr[1] == 1:
           return 1
       else:
           return 0
   if arr[2] == 0:
       return 1+jumpingFrog(arr[2:])
   if arr[2] == 1:
       return 1+jumpingFrog(arr[1:])

n = int(input("Enter n:"))
arr =[]
for i in range(n):
    arr.append(int(input()))
ans = jumpingFrog(arr)
print(ans)