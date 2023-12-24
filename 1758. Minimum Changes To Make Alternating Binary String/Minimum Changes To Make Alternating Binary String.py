class Solution:
    def minOperations(self, s: str) -> int:
        zerost = 0
        onest = 1
        zeroct = 0
        onect = 0
        for i in s:
            if i != str(zerost):
                zeroct = zeroct + 1
            if i != str(onest):
                onect = onect + 1
            zerost = (zerost + 1) % 2
            onest = (onest + 1) % 2
        return min(zeroct,onect)
