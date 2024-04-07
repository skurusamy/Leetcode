def handOfStraight(cards,w):
    if len(cards) % w != 0:
        return False
    cards.sort()
    output = []
    print(cards)
    while(cards):
        x =cards.pop(0)
        temp =[]
        temp.append(x)
        for i in range(1,w):
            if x + i not in cards :
                return False
            temp.append(x+i)
            cards.remove(x+i)
        output.append(temp)
    return output

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(handOfStraight(hand,groupSize))
#print(handOfStraight([1],1))