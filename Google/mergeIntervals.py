def merge( intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        intervals = sorted(intervals,key=lambda x: x[0])
        for interval in intervals:
            if len(output) == 0 or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1],interval[1])
        return output




intervals = [[1,3],[8,10],[2,6],[15,18]]
print(merge(intervals))