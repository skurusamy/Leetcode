# https://leetcode.com/problems/flood-fill/

'''
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
'''

def fillColor(image, i, j, newColor,color):
    if i < 0 or j >= len(image[0]) or j < 0 or i >= len(image) or image[i][j]!=color:
        return
    image[i][j] = newColor
    fillColor(image,i-1,j,newColor,color)
    fillColor(image,i,j-1,newColor,color)
    fillColor(image,i,j+1,newColor,color)
    fillColor(image,i+1,j,newColor,color)

image = [[0,0,0],[0,0,0]]
sr = sc = 0
newColor = 1
if image[sr][sc] == newColor:
    print(image)
fillColor(image,sr,sc,newColor,image[sr][sc])
print(image)