class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        check = set()
        for i in counts:
            if counts[i] in check:
                return False
            check.add(counts[i])
        return True
