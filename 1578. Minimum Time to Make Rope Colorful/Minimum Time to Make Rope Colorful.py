class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n=len(colors)
        l=0
        result=0
        for r in range(n):
            if (colors[r]!=colors[l]):
                sameColors=neededTime[l:r]
                result = result + sum(sameColors)-max(sameColors)
                l=r
        result = result + sum(neededTime[l:])-max(neededTime[l:])
        return result
