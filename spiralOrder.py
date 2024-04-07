def spiralOrder( matrix) :
        top = 0
        bottom = len(matrix) -1
        left = 0
        right = len(matrix[0]) -1
        ans = []
        while len(ans) < (len(matrix[0]) *len(matrix)):
            for x in range(left, right+1):
                if len(ans) < (len(matrix[0]) *len(matrix)):
                    ans.append(matrix[top][x])
            top += 1
            for x in range(top,bottom+1):
                if len(ans) < (len(matrix[0]) *len(matrix)):
                    ans.append(matrix[x][right])
            right -= 1
            for x in range(right,left-1, -1):
                if len(ans) < (len(matrix[0]) *len(matrix)):
                    ans.append(matrix[bottom][x])
            bottom -= 1
            for x in range(bottom, top-1, -1):
                if len(ans) < (len(matrix[0]) *len(matrix)):
                    ans.append(matrix[x][left])
            left += 1
        return ans
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))