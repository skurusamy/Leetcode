
class Solution:
    def __init__(self) -> None:
        self.valid ={0:0,1:1,6:9,8:8,9:6}

    def confusingNumberHelper(self,n):
        ans = 0
        initial_n = n
        while(n):
            rem = n % 10
            n = n // 10
            if rem not in self.valid:
                return False
            ans = (ans * 10 ) + self.valid[rem]
        return not ans == initial_n
    def confusingNumber(self,n):
        output ={}
        
        def dfs(val):
            if val > n:
                return
            if val != 0:
                if(self.confusingNumberHelper(val)):
                    if val not in output:
                        output[val] = self.confusingNumberHelper(val)
                dfs(val * 10 )
            dfs(val * 10 + 1)
            dfs(val* 10 + 6)
            dfs(val* 10 + 8)
            dfs(val * 10 + 9)
        dfs(0)
        return len(output)
        


s = Solution()
print(s.confusingNumberHelper(168))
print(s.confusingNumber(20))
