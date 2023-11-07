import heapq

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive = []
        n = len(dist)
        for i in range(n):
            time = dist[i] // speed[i]
            if (speed[i] * time < dist[i]):
                time = time + 1
            heapq.heappush(arrive,time)
        for i in range(n):
            next_arrive = heapq.heappop(arrive)
            if (next_arrive <= i):
                return i
        return n
