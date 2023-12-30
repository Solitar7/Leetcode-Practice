class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chars = [0] * 26
        for i in words:
            for x in i:
                chars[ord(x) - ord('a')] += 1
        n = len(words)
        for i in chars:
            if i % n != 0:
                return False
        return True
