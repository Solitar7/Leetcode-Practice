class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result = 0
        checklist = dict()
        for i in nums:
            check = i - int(str(i)[::-1])
            if check in checklist:
                result = result + checklist[check]
                checklist[check] = checklist[check] + 1
            else:
                checklist[check] = 1
        return result % (10**9 + 7)
