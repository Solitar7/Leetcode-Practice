class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = dict()
        result = 0
        for i in s:
            if i not in count:
                for j in count:
                    count[j][1].add(i)
                count[i] = [0,set()]
            else:
                count[i][0] = len(count[i][1])
                for j in count:
                    count[j][1].add(i)
        for i in count:
            result = result + count[i][0]
        return result
