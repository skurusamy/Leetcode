def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        using sliding window and two pointers
        """
        
        a_pointer = b_pointer = 0
        max_len = 0
        charSet = set()
        while b_pointer < len(s):
            if s[b_pointer] not in charSet:
                charSet.add(s[b_pointer])
                b_pointer += 1
                max_len = max(len(charSet), max_len)
            else:
                charSet.remove(s[a_pointer])
                a_pointer += 1
        return max_len

print(lengthOfLongestSubstring("abcabcbb"))