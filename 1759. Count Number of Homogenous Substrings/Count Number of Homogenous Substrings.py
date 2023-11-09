class Solution:
    def countHomogenous(self, s: str) -> int:
        total = 0
        count = 0
        curr = s[0]
        for i in s:
            if curr != i:
                curr = i
                count = 0
            count = count + 1
            total = total + count
        return (total % (10**9 + 7))
