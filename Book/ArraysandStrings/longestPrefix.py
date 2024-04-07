def longestPrefix(arr):
    ans =""
    i = 0
    firstWord = arr[0]
    for c in range(len(firstWord)):
        for otherwords in range(1, len(arr)):
            if i >= len(arr[otherwords]) or firstWord[c] != arr[otherwords][i]:
                return ans
        ans += firstWord[c]
        i += 1
    print(ans)


arr = ["su","subh","subha"]
longestPrefix(arr)