class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        idx = defaultdict(list)
        for i,c in enumerate(s):
            idx[c].append(i)
        ans = 0
        for c,i in idx.items():
            if len(i) < 2:
                continue
            if len(i) > 2:
                ans += 1
            for k,j in idx.items():
                if c == k:
                    continue
                if bisect_left(j, i[0]) < bisect_left(j, i[-1]):
                    ans += 1
        return ans
