class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = float("inf")
        second = float("inf")
        for i in prices:
            if i < second:
                if i < first:
                    second = first
                    first = i
                else:
                    second = i
        result = money - first - second
        if result < 0:
            return money
        else:
            return result
