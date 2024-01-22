class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        check = set()
        for i in range(len(nums)):
            if nums[i] not in check:
                check.add(nums[i])
            else:
                result.append(nums[i])
        for i in range(len(nums)):
            if i+1 not in check:
                result.append(i+1)
        return result
