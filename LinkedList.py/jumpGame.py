nums = [2,3,1,1,4]
#nums =[0]
goodPlace = len(nums)-1
for i in range(len(nums)-1,-1,-1):
    if nums[i] + i >= goodPlace:
        goodPlace = i
print(goodPlace == 0)