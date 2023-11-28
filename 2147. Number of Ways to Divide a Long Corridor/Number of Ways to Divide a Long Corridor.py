class Solution:
    def numberOfWays(self, corridor: str) -> int:
        result = 1
        Scount = 0
        between = 0
        for i in range(len(corridor)):
            if corridor[i] == "S":
                Scount = Scount + 1
            elif (corridor[i] == "P") and (Scount == 2):
                between = between + 1
            if Scount == 4:
                result = result * (between + 1)
                between = 0
                Scount = 2
        if Scount != 2:
            return 0
        return result % (10**9 + 7)
