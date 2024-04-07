def is_palindrome(s):
    left = 0
    right = len(s) -1 
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        if left == right:
            return True
    return False

print(is_palindrome("kayak"))
