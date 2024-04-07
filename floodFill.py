def floodFillHelper(image,i,j,color,newColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != color:
            return
        image[i][j] = newColor
        floodFillHelper(image,i-1,j,color,newColor)
        floodFillHelper(image,i+1,j,color,newColor)
        floodFillHelper(image,i,j-1,color,newColor)
        floodFillHelper(image,i,j+1,color,newColor)
        
def floodFill( image, sr, sc: int, newColor: int) :
        if image[sr][sc] == newColor:
            return image
        floodFillHelper(image,sr,sc,image[sr][sc],newColor)
        return image

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2

print(floodFill(image, sr, sc, newColor))