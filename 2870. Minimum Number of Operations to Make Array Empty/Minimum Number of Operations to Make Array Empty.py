class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = dict()
        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1
        result = 0
        for i in counts:
            if counts[i] == 1:
                return -1
            if counts[i] % 3 == 0:
                result += + counts[i]//3
            else:
                result += counts[i]//3 + 1
        return result
