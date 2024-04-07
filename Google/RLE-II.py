class RLEIterator(object):
    
    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.arr = encoding

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = n
        i=0
        while(i < len(self.arr) and counter <= n):
                if self.arr[i] >= counter:
                    self.arr[i] = self.arr[i] - counter
                    counter = self.arr[i]
                    return self.arr[i+1]
                else:
                    counter = counter - self.arr[i]
                    self.arr[i] = 0
                    
                i += 2
        return -1
r = RLEIterator([811,903,310,730,899,684,472,100,434,611])

n = [358,345,154,265,73,220,138,4,170,88]
#n = [358]
for i in n:
    print(r.next(i))