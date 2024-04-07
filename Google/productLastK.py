class ProductOfNumbers:
    
    def __init__(self):
        self.prod_arr = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prod_arr = [1]
        else:
            self.prod_arr.append(self.prod_arr[-1] * num)
        print(self.prod_arr)    

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        
        if len(self.prod_arr) - 1 >= k:
            prod = self.prod_arr[-1] // self.prod_arr[len(self.prod_arr)-k-1]
            return prod
        else:
            return 0
        

p = ProductOfNumbers()
p.add(3)
p.add(0)
p.add(2)
p.add(5)
p.add(4)
print(p.getProduct(2))
