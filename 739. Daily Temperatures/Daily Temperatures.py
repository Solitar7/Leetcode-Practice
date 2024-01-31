class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        result = []
        for i in range(len(temperatures)):
            while len(days) > 0:
                if days[0][0] < temperatures[i]:
                    result[days[0][1]] = i - days[0][1]
                    heapq.heappop(days)
                else:
                    break
            result.append(0)
            heapq.heappush(days,(temperatures[i],i))
        return result
