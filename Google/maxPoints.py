def maxScore(cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if len(cardPoints) == k:
            return sum(cardPoints)
        m = len(cardPoints) - k
        mini = curMini = sum(cardPoints[:m])
        for i in range(len(cardPoints)-m):
            curMini  -= cardPoints[i]
            curMini += cardPoints[i+m]
            mini = min(curMini,mini)
        return sum(cardPoints) - mini

cardPoints = [1,2,3,4,5,6,1]
k = 3
#cardPoints=[2,2,2]
#k = 2
print(maxScore(cardPoints,k))