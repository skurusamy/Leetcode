import sys
def sunsetViews(buildings, direction):
    # Write your code here.
    output = set()
    if direction == 'WEST':
        buildings.reverse()
    maxi = - sys.maxsize
    for i in range(len(buildings)-1,-1,-1):
    	if buildings[i] > maxi:
            if direction == 'WEST':
                val = len(buildings)-1 - i
                print(val)
                output.add(val)
            else:
                output.add(i)
            maxi = buildings[i]  
    return output   

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2],"WEST"))