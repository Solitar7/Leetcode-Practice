# Checked some others' idea for help in shortestPath
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.allE = dict()
        for i in edges:
            if i[0] in self.allE:
                self.allE[i[0]].append((i[1],i[2]))
            else:
                self.allE[i[0]] = [(i[1],i[2])]
            if i[1] not in self.allE:
                self.allE[i[1]] = []

    def addEdge(self, edge: List[int]) -> None:
        if edge[0] in self.allE:
            self.allE[edge[0]].append((edge[1],edge[2]))
        else:
            self.allE[edge[0]] = [(edge[1],edge[2])]
        if edge[1] not in self.allE:
            self.allE[edge[1]] = []

    def shortestPath(self, node1: int, node2: int) -> int:
        if (node1 == node2):
            return 0

        if (node1 not in self.allE) or (node2 not in self.allE):
            return -1
        
        dist = [float('inf')] * 101
        dist[node1] = 0

        paths = []
        heapq.heappush(paths,(0,node1))
        while (len(paths) > 0):
            curr = heapq.heappop(paths)
            if (curr[1] == node2):
                return curr[0]
            for i in self.allE[curr[1]]:
                if dist[i[0]] > dist[curr[1]] + i[1]:
                    dist[i[0]] = dist[curr[1]] + i[1]
                    heapq.heappush(paths,(dist[i[0]],i[0]))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
