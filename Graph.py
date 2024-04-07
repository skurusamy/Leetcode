from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.allNode = []
    def addEdge(self, first,second):
        self.graph[first].append(second)
        if first not in self.allNode:
            self.allNode.append(first)
        if second not in self.allNode:
            self.allNode.append(second)
    
    def dfsHelper(self,visited, node):
        if visited[self.allNode.index(node)] == False:
            visited[self.allNode.index(node)] = True
            print(node,end=" ")
            if node in self.graph.keys():
                for neigh in self.graph[node]:
                    if visited[self.allNode.index(neigh)] == False:    
                        self.dfsHelper(visited, neigh)
    def dfs(self):
        visited = [False] * (len(self.allNode))
        for node in self.graph.keys():
            if visited[self.allNode.index(node)] == False:
                self.dfsHelper(visited,node)
    
    def dfsItr(self,visited):
        stack = []
        for node in self.graph.keys():
            if visited[self.allNode.index(node)] == False:
                visited[self.allNode.index(node)] = True
                stack = [node]
                while stack:
                    curr = stack.pop()
                    print(curr)
                    if curr in self.graph.keys():
                        for neigh in self.graph[curr]:
                            if visited[self.allNode.index(neigh)] == False:
                                visited[self.allNode.index(neigh)] = True
                                stack.append(neigh)

    def bfsItr(self,visited):
        queue =[]
        for node in self.graph.keys():
            if visited[self.allNode.index(node)] == False:
                visited[self.allNode.index(node)] = True
                queue = [node,]
                while queue:
                    curr = queue.pop(0)
                    print(curr,end=",")
                    if curr in self.graph.keys():
                        for neigh in self.graph[curr]:
                            if visited[self.allNode.index(neigh)] == False:
                                visited[self.allNode.index(neigh)] = True
                                queue.append(neigh)
                           

g = Graph()
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(5,4)
#print(g.graph,g.allNode)
visited = [False] * len(g.allNode)
#g.dfs()
#g.dfsItr(visited)
g.bfsItr(visited)