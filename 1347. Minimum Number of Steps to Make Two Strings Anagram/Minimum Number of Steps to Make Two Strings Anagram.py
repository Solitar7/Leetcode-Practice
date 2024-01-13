class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = dict()
        for i in s:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        for i in t:
            if i not in counts:
                counts[i] = 0
            counts[i] -= 1
        diff = 0
        for i in counts:
            diff += abs(counts[i])
        return diff // 2
