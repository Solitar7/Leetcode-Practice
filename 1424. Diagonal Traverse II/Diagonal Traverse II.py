class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        mp = dict()
        result = list()
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in mp:
                    mp[i+j] = [nums[i][j]]
                else:
                    mp[i+j].append(nums[i][j])
        for i in mp:
            for j in range(len(mp[i])):
                result.append(mp[i][len(mp[i])-j-1])
        return result
