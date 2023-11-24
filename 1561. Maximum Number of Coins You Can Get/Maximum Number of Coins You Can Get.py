class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        i = len(piles)//3
        while i < len(piles):
            result = result + piles[i]
            i = i + 2
        return result
