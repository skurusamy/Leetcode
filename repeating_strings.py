"""
Sample Input 0
aba
10
Sample Output 0
7
Explanation 0
The first n=10  letters of the infinite string are abaabaabaa. Because there are 7 a's, we return 7.
"""

s = input("Enter a string: ")
n = int(input("Enter the number:" ))
count_a = s.count('a')
chunks = n // len(s)
if n % len(s) == 0:
    ans = count_a * chunks
else:
    rem = n%len(s)
    ans = (count_a * chunks) + (s[:rem].count('a')) # (s[:rem].count('a')) -> check 'a' in last chunk
print(ans)