class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 1
        kNeed = 0
        end = 0
        i = 1
        while i < len(nums):
            kNeed = kNeed + (i - end) * (nums[i] - nums[i-1])
            while kNeed > k:
                kNeed = kNeed - (nums[i] - nums[end])
                end = end + 1
            result = max(result, (i - end + 1))
            i = i + 1
        return result
