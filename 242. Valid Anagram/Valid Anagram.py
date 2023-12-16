class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in t:
            if i in count:
                count[i] -= 1
                if count[i] < 0:
                    return False
            else:
                return False
        for i in count:
            if count[i] > 0:
                return False
        return True
