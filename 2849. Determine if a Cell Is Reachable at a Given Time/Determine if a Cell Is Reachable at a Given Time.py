class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if ((sx == fx) and (sy == fy) and (t == 1)):
            return False
        XD = abs(sx - fx)
        YD = abs(sy - fy)
        if (max(XD,YD,t) <= t):
            return True
        return False
