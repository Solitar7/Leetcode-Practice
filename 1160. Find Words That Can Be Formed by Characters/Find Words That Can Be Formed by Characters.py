class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for i in words:
            add = True
            for j in i:
                if i.count(j) > chars.count(j):
                    add = False
                    break
            if add:
                result = result + len(i)
        return result
