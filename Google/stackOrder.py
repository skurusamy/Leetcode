def validateStackSequences(pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack =[]
        j =0
        for i in pushed:
            stack.append(i)
            while(stack)  and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed, popped))