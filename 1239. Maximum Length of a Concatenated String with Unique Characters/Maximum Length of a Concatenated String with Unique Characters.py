class Solution:
    def maxLength(self, arr: List[str]) -> int:
        combinations = [""]
        maxL = 0
        for word in arr:
            for c in combinations:
                new_comb = c + word
                if len(new_comb) == len(set(new_comb)):
                    combinations.append(new_comb)
                    maxL = max(maxL,len(new_comb))
        return maxL
