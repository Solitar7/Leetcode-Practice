class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                lower = stack.pop()
                ret[lower[1]] = i - lower[1]
            stack.append((temp,i))
        return ret
