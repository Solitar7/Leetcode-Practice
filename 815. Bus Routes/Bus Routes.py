class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stations = list()
        for i in range(10**6):
            stations.append(list())
        for i in range(len(routes)):
            for j in routes[i]:
                stations[j].append(i)
        newSt = [source]
        reachable = [False]*(10**6)
        reachableRoute = [False]*500
        busnum = 0
        while(len(newSt) > 0):
            nextNew = []
            for i in newSt:
                if i == target:
                    return busnum
                reachable[i] = True
                newRoute = []
                for j in stations[i]:
                    if not reachableRoute[j]:
                        newRoute.append(j)
                        reachableRoute[j] = True
                for k in newRoute:
                    for l in routes[k]:
                        if not reachable[l]:
                            if l == target:
                                return busnum + 1
                            nextNew.append(l)
            newSt = nextNew
            busnum = busnum + 1
        return -1
