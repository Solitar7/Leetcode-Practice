class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        r = n % 7
        result = (w * (w-1) // 2) * 7 + w * 28
        result = result + (r * (r+1) // 2) + w * r
        return result
