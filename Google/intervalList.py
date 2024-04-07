def intervalIntersection( firstList, secondList):
    ans =[]
    pA = 0
    pB = 0
    while (pA < len(firstList) and pB < len(secondList)):
        begin = max(firstList[pA][0],secondList[pB][0])
        end = min(firstList[pA][1],secondList[pB][1])
        if begin <= end:
            output = [begin,end]
            ans.append(output)
        if firstList[pA][1] < secondList[pB][1]:
            pA += 1
        else:
            pB += 1



    return ans


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
#output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

print(intervalIntersection( firstList, secondList))