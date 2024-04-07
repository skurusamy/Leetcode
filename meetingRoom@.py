import heapq
class interval:
    def __init__(self,s,e):
        self.end = e
        self.start = s

def minMeetingRooms(intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # sort the intervals by start time
        intervals.sort(key=lambda x: x.start)
        #print(intervals[1].start)
        heap = []
        for interval in intervals:
            print(heap)
            if heap and interval.start >= heap[0]:

                heapq.heapreplace(heap, interval.end)

            else:
                heapq.heappush(heap, interval.end)
        
        return len(heap)

in1 = interval(0, 30)
in2 = interval(15, 20)
in3 = interval(5, 10)
intervals = [in1,in2,in3]
print(minMeetingRooms(intervals))
