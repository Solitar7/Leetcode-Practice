class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counts = {}
        result = []
        for i in nums:
            if i not in counts:
                counts[i] = 0
            if counts[i] == len(result):
                result.append([])
            result[counts[i]].append(i)
            counts[i] += 1
        return result
