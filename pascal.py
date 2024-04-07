def generate( numRows: int):
        ans =[]
        for row in range(numRows):
                subArr = [1] * (row+1)
                for i in range(1,row):
                    subArr[i] = ans[row-1][i-1] + ans[row-1][i]
                ans.append(subArr)
        return ans

print(generate(5))