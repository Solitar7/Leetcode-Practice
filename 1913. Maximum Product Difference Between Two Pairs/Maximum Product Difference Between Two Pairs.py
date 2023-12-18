class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_first = -1
        max_second = -1
        min_first = float('inf')
        min_second = float('inf')

        for i in nums:
            if i < min_second:
                if i < min_first:
                    min_second = min_first
                    min_first = i
                else:
                    min_second = i
            if i > max_second:
                if i > max_first:
                    max_second = max_first
                    max_first = i
                else:
                    max_second = i
        return (max_first * max_second) - (min_first * min_second)
