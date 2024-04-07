from collections import defaultdict 
def buildSequence(sorted_array,i,newDisk,heights):
    disks = sorted_array[i]
    if len(disks) == 0:
        sorted_array[i].append(newDisk)
        heights[i] += newDisk[2]
        return
    for j in range(len(disks)):
        if disks[j][0] < newDisk[0] and disks[j][1] < newDisk[1]:
            sorted_array[i].append(newDisk)
            heights[i] += newDisk[2]
        else:
            if heights[i] < heights[i] + newDisk[2]:
                sorted_array[i].remove(disks[j])
                sorted_array[i].append(newDisk)
                heights[i] += newDisk[2]
    return      
def diskStacking(disks):
    # Write your code here.
    disks = sorted(disks, key= lambda x:x[2])
    heights = []
    for i in disks:
        heights.append(i[2])
    sorted_array = defaultdict(list)
    for i in range(len(disks)):
        cur_disk = disks[i]
        for j in range(i):
            another_disk = disks[j]
            if cur_disk[0] > another_disk[0] and cur_disk[1] > another_disk[1]:
                if heights[i] <= heights[i] + another_disk[2] :
                    buildSequence(sorted_array,i,another_disk,heights)     
        sorted_array[i].append(cur_disk)
        
    print(sorted_array)

disks = [
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]
  ]
print(diskStacking(disks))