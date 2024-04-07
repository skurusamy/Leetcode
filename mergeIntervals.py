from tracemalloc import start


class Interval:
    def __init__(self,start,end) :
        self.start = start
        self.end = end

def merge(intervals):
    intervals.sort(key=lambda x:x.start)
    mergedInterval =[]
    start = intervals[0].start
    end = intervals[0].end
    for i  in range(1,len(intervals)):
        if intervals[i].start <=  end:
            end = max(intervals[i].end,end)
        else:
            mergedInterval.append(Interval(start,end))
            start = intervals[i].start
            end = intervals[i].end

    mergedInterval.append(Interval(start,end))
    return mergedInterval

def PrintIntervals(arr):
    for ele in arr:
        print((ele.start,ele.end),end =" ")


def insertIntervals(intervals,newInterval):
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if newInterval.start < interval.end: 
            start = min(newInterval.start,interval.start)
            end = max(newInterval.end,interval.end)
            interval.start = start
            interval.end = end
            return intervals

intervals = [Interval(1, 3), Interval(5,7), Interval(8, 12)]
ans = merge(intervals)
PrintIntervals(ans)
print("\nInsert new Interval")
result = insertIntervals(intervals,Interval(4,6))
PrintIntervals(result)
