class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        one = -1
        two = -1
        for i in nums:
            if i > one:
                two = one
                one = i
            elif i > two:
                two = i
        return (one - 1) * (two - 1)
