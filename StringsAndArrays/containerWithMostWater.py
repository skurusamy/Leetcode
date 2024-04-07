def containerWithMaxWater(height):
    a_pointer = 0
    b_pointer = len(height) -1
    maxArea = -999999
    while a_pointer < b_pointer:
        if height[a_pointer] < height[b_pointer]:
            area = (b_pointer - a_pointer) * height[a_pointer]
            a_pointer += 1
        else:
            area = (b_pointer - a_pointer) * height[b_pointer]
            b_pointer -= 1
        maxArea = max(area,maxArea)
    return maxArea


height = [1,8,6,2,5,4,8,3,7]
print(containerWithMaxWater(height))