class Solution:
    def rob(self, nums: List[int]) -> int:
        last = 0
        curr = nums[0]
        for i in range(1,len(nums)):
            new = max(curr,last+nums[i])
            last = curr
            curr = new
        return curr
