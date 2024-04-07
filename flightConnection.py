from collections import defaultdict
class Routes:
    def __init__(self):
        self.routes = defaultdict(list)
    def addRoutes(self,origin,destination):
        self.routes[origin].append(destination)

    def validateRoute(self,origin,dest):
        visited = set()
        if origin not in self.routes.keys():
            return False
        def dfs(origin,dest):
            print(origin,dest)
            if dest in self.routes[origin]:
                return True
            visited.add(origin)
            for i in self.routes[origin]:
                if origin in visited:
                    return False
                return dfs(i,dest)
            if len(visited) == len(self.routes.keys()):
                return False
        return dfs(origin,dest)


        
            
            


r = Routes()
r.addRoutes("IND", "USA")
r.addRoutes("USA", "IND")
r.addRoutes("FRA", "CHI")
r.addRoutes("FRA", "MEX")
r.addRoutes("FRA", "DXB")
r.addRoutes("CHI", "IND")
r.addRoutes("IND", "CHI")
r.addRoutes("USA","CHI")

print(r.routes)

print(r.validateRoute('FRA','IND'))