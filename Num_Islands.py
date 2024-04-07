'''
Count the number of islands in the given grid
Given 2d grid with 0-water and 1  - land 
island is sorrounded by water and is formed by corresponding lands surrounded horizontally vertically

'''
def dfs(ip,i,j):
    # error case
    # check boundries
    if(i < 0 or j<0 or i>= len(ip) or j >= len(ip[i]) or ip[i][j] == 0):
        return 0
    # which checking the particular element - checking its vertical and horizontal elements so we donnt recount it
    ip[i][j]=0
    dfs(ip,i+1,j)
    dfs(ip,i-1,j)
    dfs(ip,i,j-1)
    dfs(ip,i,j+1)
    return 1

#main
#ip =[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
ip =[[1,1,1,1,0],
    [1,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0]]
#check every element in the matrix - so nested loop
numIsland = 0
for i in range(len(ip)):
    for j in range(len(ip[i])):
        if(ip[i][j]==1): #only if  value is 1 - we have to do something - else ignore and its implemented using dfs or  bfs
            numIsland += dfs(ip,i,j)
print(numIsland)