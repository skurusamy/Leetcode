from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getDistance(point):
    return point.x ** 2 + point.y ** 2


def kClosest(points, k):
    distance = defaultdict(list)
    count = 0
    kpoints = []
    for point in points:
        dist = getDistance(point)
        distance[dist].append(point)
    for i in sorted(distance):
        kpoints.append(distance[i])
        count += 1
        if count == k:
            #print(distance)
            return kpoints


p1 = Point(4, 6)
p2 = Point(4, 7)
p3 = Point(4, 4)
p4 = Point(2, 5)
p5 = Point(1, 1)

points = [p1, p2, p3, p4, p5]
k = 3
l =[]
l= kClosest(points, k)
for i in range(len(l)):
    print(l[i][0].x,l[i][0].y)

