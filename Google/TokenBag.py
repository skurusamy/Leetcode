'''
Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.

Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.

'''
def bagofTokens(tokens, power):
    tokens.sort()
    i =0 
    j = len(tokens) -1
    maxPoints = 0
    points = 0
    while (i <=j):
        if power >= tokens[i]:
            points += 1
            power -= tokens[i]
            i += 1
            maxPoints = max(maxPoints,points)
        elif points > 0:
            points -= 1
            power += tokens[j]
            j -= 1
        else:
            return maxPoints
    return maxPoints
print(bagofTokens([100,200,300,400],200))