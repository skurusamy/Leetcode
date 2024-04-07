from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.allNodes = []
    def addEdge(self,first,second):
        if first is None and second is None:
            return
        if second not in self.graph[first]:
            self.graph[first].append(second)
        if first not in self.allNodes:
            self.allNodes.append(first)
        if second not in self.allNodes:
            self.allNodes.append(second)
    def printAllNodes(self):
        print(self.allNodes)
    def dfs(self,visited):
        for node in list(self.graph.keys()):
            if visited[self.allNodes.index(node)] == False:
                self.dfsHelper(node,visited)
    def dfsHelper(self,node,visited):
        if visited[self.allNodes.index(node)] == False:
            visited[self.allNodes.index(node)] = True
            print(node,end=" ")
        for neigh in self.graph[node]:
            if visited[self.allNodes.index(neigh)] == False:
                self.dfsHelper(neigh,visited)
    def dfsItr(self,visited):
        stack =[]
        for nodes in list(self.graph.keys()):
            if visited[self.allNodes.index(nodes)] == False:
                visited[self.allNodes.index(nodes)] = True
                stack.append(nodes)
                while(stack):
                    curr = stack.pop()
                    print(curr, end=" ")
                    for neigh in self.graph[curr]:
                        if visited[self.allNodes.index(neigh)] == False:
                            visited[self.allNodes.index(neigh)] = True
                            stack.append(neigh)
    def bfsItr(self,visited):
        queue =[]
        for nodes in list(self.graph.keys()):
            if visited[self.allNodes.index(nodes)] == False:
                visited[self.allNodes.index(nodes)] = True
                queue.append(nodes)
                while queue:
                    curr = queue.pop(0)
                    print(curr, end=" ")
                    for neigh in self.graph[curr]:
                        if visited[self.allNodes.index(neigh)] == False:
                            visited[self.allNodes.index(neigh)] = True
                            queue.append(neigh)
    def mdfs(self,visited):
        output = []
        for node in list(self.graph.keys()):
            output.append(node)
            self.dfsHelper(node,visited)
        #for i in range(len(output)-1,-1,-1):
            #print(output[i],end=" ")
    def kahns(self):
        indegree = [0] * len(self.allNodes)
        for val in self.graph.values():
            for v in val:
              indegree[self.allNodes.index(v)] += 1
        #print(self.allNodes)
        #print(indegree)
        queue = []
        for nodes in list(self.graph.keys()):
            if indegree[self.allNodes.index(nodes)] == 0:
                queue.append(nodes)
                while queue:
                    for neigh in self.graph[nodes]:
                        indegree[self.allNodes.index(neigh)] -= 1
                    print(queue.pop(0),end=" ")


g = graph()
g.addEdge(1,2)
g.addEdge(2,5)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(5,4)
print(g.graph)
visited = [False] * len(g.allNodes)
g.dfs(visited)
print("\n")
visited = [False] * len(g.allNodes)
g.bfsItr(visited)
'''
g.mdfs(visited)
print("\n")
g.kahns()
'''