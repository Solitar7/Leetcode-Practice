class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        for i in range(len(nums) - 1):
            j = i+1
            while j < len(nums):
                if(nums[i] + nums[j] == target):
                    result[0] = i
                    result[1] = j
                j = j+1
        return result
