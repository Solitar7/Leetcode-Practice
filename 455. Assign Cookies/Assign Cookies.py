class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        i = 0
        j = 0
        while i < len(g):
            while j < len(s):
                if g[i] <= s[j]:
                    count = count + 1
                    j = j + 1
                    break
                else:
                    j = j + 1
            i = i + 1
        return count
