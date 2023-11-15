class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        count = 1
        for i in arr[1:]:
            if (i > count):
                count = count + 1
        return count
