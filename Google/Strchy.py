def findOccur(word):
    letters =[]
    count = []
    for c in word:
        if not letters or c != letters[-1]:
            letters.append(c)
            count.append(1)
        else:
            count[-1] += 1
    print(letters,count)
    return (letters,count)

def expressiveWords(s, words):
        sLetters,sCount = findOccur(s)
        ans = 0
        for word in words:
            wLetters,wCount = findOccur(word)
            def isStrchy(word):
                if sLetters != wLetters:
                    return False
                for c in range(len(sCount)):
                    if sCount[c] < 3 and sCount[c] != wCount[c]:
                        return False
                    if sCount[c] >= 3 and sCount[c] < wCount[c]:
                        return False
                return True
            if isStrchy(word):
                ans += 1
        return ans
s = "heeellooo"
words = ["hello", "hi", "helo"]
print(expressiveWords(s, words))