'''
Count the number of battleship in the given grid
Given 2d grid with X-battleship and .  - nothing 
Battle ship can be only found vertically or horizontally

valid battleship        invalid
X . X                   . . X
. . X                   X X X
. . X                   . . X

Can be done in iterative or recurrsive
'''
'''
#iterative
battleship = [['X','.','X'],['.','.','X'],['.','.','X']]
count =0
#go through all the elements and increment if you find a new  battleship
for i in range(len(battleship)):
    for j in range(len(battleship[i])):
        if battleship[i][j] == '.':
            continue
        if i>0 and battleship[i-1][j] == 'X': # continuty of same battleship 
            continue
        if j> 0 and battleship[i][j-1] == 'X': 
            continue
        count += 1
print(count)
'''
def sink(battleship,i,j):
    if i < 0 or j < 0 or i >= len(battleship) or j >= len(battleship) or battleship[i][j] == '.':
        return
    battleship[i][j] = '.'
    sink(battleship,i-1,j)
    sink(battleship,i+1,j)
    sink(battleship,i,j-1)
    sink(battleship,i,j+1)
#recurrsive  -- traverse through each X and sink its neighbours 
battleship = [['X','.','X'],['.','.','X'],['.','.','X']]
count =0
for i in range(len(battleship)):
    for j in range(len(battleship[i])):
        if battleship[i][j] == 'X':
            count += 1
            #call its neighbouring element and sink that.
            sink(battleship,i,j)
print(count)
        

