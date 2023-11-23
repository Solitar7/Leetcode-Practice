class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = list()
        for i in range(len(l)):
            check = nums[l[i]:r[i]+1]
            check.sort()
            checkAs = True
            for i in range(2,len(check)):
                if (check[i] - check[i-1]) != (check[1] - check[0]):
                    checkAs = False
                    break
            result.append(checkAs)
        return result
