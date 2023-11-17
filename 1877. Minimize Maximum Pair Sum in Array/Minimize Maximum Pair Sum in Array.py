class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxSum = 0
        n = len(nums)
        end = n/2
        i = 0
        while (i < end):
            if (maxSum < (nums[i] + nums[n-1-i])):
                maxSum = nums[i] + nums[n-1-i]
            i = i + 1
        return maxSum
