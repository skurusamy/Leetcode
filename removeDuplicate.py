def removeElement(nums, val):
        ans = []
        i = 0
        j = len(nums) - 1

        while i < j:
            while nums[i] != val:
                i += 1
            while nums[j] == val:
                j -= 1
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
            ans = j + 1
        return nums[:j+1]

print(removeElement([1,2,1],1))