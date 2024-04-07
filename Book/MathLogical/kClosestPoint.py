from collections import defaultdict
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getDistance(point):
    return point.x ** point.x + point.y ** point.y
def kClosest(points,k):
    ans =[]
    count =0
    dic = defaultdict(list)
    for point in points:
        dis=getDistance(point)
        dic[dis].append(point)
    print(dic)
    for i in sorted(dic):
        ans.append(dic[i])
       # print(ans)
        count += 1
        if count == k:
            return ans
        


p1 = Point(4, 6)
p2 = Point(4, 7)
p3 = Point(4, 4)
p4 = Point(2, 5)
p5 = Point(1, 1)
ans =[]
points = [p1, p2, p3, p4, p5]
k = 4
ans =kClosest(points,3)
#print(ans)
for point in range(len(ans)):
    print(ans[point][0].x,ans[point][0].y)