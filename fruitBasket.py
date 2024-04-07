def totalFruit(fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        if len(fruits) <= 2:
            return len(fruits)
        start = 0
        end = 0
        count = 0
        temp = set()
        map = {}
        while end < len(fruits):
            if len(temp) < 2:
                count += 1
                temp.add(fruits[end])
                end += 1 
            elif fruits[end] in temp:
                count += 1
                temp.add(fruits[end])
                end += 1 
            else:
                map[start] = count
                start = end -1
                end = end -1
                temp = set()
                count = 0
        return max(map.values())

print(totalFruit([1,2,1]))