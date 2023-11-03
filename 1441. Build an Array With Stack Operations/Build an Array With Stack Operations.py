class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        last = 0
        for i in target:
            skip = i - last - 1
            for j in range(skip):
                result.append("Push")
                result.append("Pop")
            result.append("Push")
            last = i
        return result
