from collections import defaultdict
def mostVisitedPattern( username, timestamp, website):
    dic = defaultdict(list)
    for i in range(len(username)):
        dic[username[i]].append(website[i])
    print(dic)


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print(mostVisitedPattern(username,timestamp,website))