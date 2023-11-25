class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        absSum = sum(nums)
        result = []
        for i in range(n):
            result.append(absSum + i * nums[i] - (n-i) * nums[i])
            absSum = absSum - 2 * nums[i]
        return result
