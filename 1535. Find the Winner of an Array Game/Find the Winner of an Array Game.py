class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        curr = arr[0]
        wins = 0
        i = 1
        while (i < len(arr)):
            if (curr > arr[i]):
                wins = wins + 1
            else:
                curr = arr[i]
                wins = 1
            if (wins == k):
                return curr
            i = i + 1
        return curr
