class RLEIterator(object):
    
    def __init__(self, encoding):
        """
        :type encoding: List[int]
        """
        self.arr = []
        i = len(encoding) - 1
        while i > 0:
            for j in range(encoding[i-1]):
                self.arr.insert(0,encoding[i])
            i-=2

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self.arr) < n:
            return -1
        for i in range(n-1):
            self.arr.pop(0)
        return self.arr.pop(0)

r = RLEIterator([3, 8, 0, 9, 2, 5])
print(r.arr)
print(r.next(2))
print(r.next(1))
print(r.next(1))
