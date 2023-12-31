class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        chars = []
        for i in range(26):
            chars.append([-1,-1])
        result = -1
        for i in range(len(s)):
            if chars[ord(s[i]) - ord('a')][0] == -1:
                chars[ord(s[i]) - ord('a')][0] = i
            else:
                chars[ord(s[i]) - ord('a')][1] = i
                result = max(result, i - chars[ord(s[i]) - ord('a')][0] - 1)
        return result
