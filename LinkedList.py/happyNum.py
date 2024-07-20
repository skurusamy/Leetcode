def happyNum(quo):
    ans = 0
    while quo > 0:
        rem = quo % 10
        quo = quo // 10
        ans += (rem*rem)
    return ans
def isHappy(num):
    slow = num
    fast = num
    while True:
        slow = happyNum(slow)
        fast = happyNum(happyNum(fast))
        if slow == fast:
            break
    return slow == 1


print(isHappy(23))