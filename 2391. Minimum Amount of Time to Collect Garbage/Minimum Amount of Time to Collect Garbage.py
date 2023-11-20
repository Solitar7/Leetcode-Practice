class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        count = [0,0,0]
        result = 0
        cost = 0
        for i in range(len(travel)):
            result = result + len(garbage[i])
            cost = cost + travel[i]
            if 'M' in garbage[i+1]:
                count[0] = cost
            if 'P' in garbage[i+1]:
                count[1] = cost
            if 'G' in garbage[i+1]:
                count[2] = cost
        result = result + len(garbage[-1]) + sum(count)
        return result
