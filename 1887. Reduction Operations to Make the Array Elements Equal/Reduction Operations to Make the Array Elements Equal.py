class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        order = list(set(nums))
        order.sort()
        count = dict()
        for i in order:
            count[i] = 0
        for i in nums:
            count[i] = count[i] + 1
        result = 0
        for i in range(len(order)):
            result = result + count[order[i]] * i
        return result
