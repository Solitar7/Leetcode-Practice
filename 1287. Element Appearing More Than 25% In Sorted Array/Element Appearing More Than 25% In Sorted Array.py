class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) // 4 + 1
        count = 0
        prev = -1
        for i in arr:
            if i == prev:
                count = count + 1
            else:
                prev = i
                count = 1
            if count >= n:
                return prev
