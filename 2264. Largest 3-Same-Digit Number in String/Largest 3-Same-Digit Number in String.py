class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = -1
        for i in range(len(num)-2):
            if ((num[i] == num[i+1]) and (num[i+1] == num[i+2])):
                result = max(int(num[i]),result)
        if result == -1:
            return ""
        return str(result)*3
