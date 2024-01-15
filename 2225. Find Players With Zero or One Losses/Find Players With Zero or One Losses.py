class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counts = dict()
        for i in matches:
            if i[0] not in counts:
                counts[i[0]] = 0
            if i[1] not in counts:
                counts[i[1]] = 1
            else:
                counts[i[1]] += 1
        result = [[],[]]
        for i in counts:
            if counts[i] == 0:
                result[0].append(i)
            elif counts[i] == 1:
                result[1].append(i)
        result[0].sort()
        result[1].sort()
        return result
