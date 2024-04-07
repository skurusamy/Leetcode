def missingIntervals(intervals):
    intervals.sort(key= lambda x: x[0])
    output = []
    endTime  = 1
    for interval in intervals:
        if endTime < interval[0]:
            output.append([endTime,interval[0]])
        endTime = max(endTime,interval[1])
    output.append([endTime,24])
    return output
intervals = [[2, 6], [2, 3], [8, 10], [15, 18]]
print(missingIntervals(intervals))