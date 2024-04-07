def fillColor(image,i,j,color,newColor):
    if i < 0 or i >=len(image) or j <0 or j>=len(image[0]) or image[i][j] != color:
        return
    image[i][j] = newColor
    fillColor(image,i+1,j,color,newColor)
    fillColor(image, i -1, j, color, newColor)
    fillColor(image, i , j+ 1, color, newColor)
    fillColor(image, i , j-1, color, newColor)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
i=0
j=0
newColor = 2
if image[sr][sc] == newColor:
    print(image)
fillColor(image,sr,sc,image[sr][sc],newColor)
print(image)