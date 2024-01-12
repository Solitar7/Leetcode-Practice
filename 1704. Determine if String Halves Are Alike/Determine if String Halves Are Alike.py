class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        half = n//2
        diff = 0
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        for i in range(half):
            if s[i] in vowels:
                diff += 1
        for j in range(half,n):
            if s[j] in vowels:
                diff -= 1
        return diff == 0
