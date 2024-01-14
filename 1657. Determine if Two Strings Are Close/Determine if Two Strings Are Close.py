class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        char1 = dict()
        char2 = dict()
        for i in word1:
            if i not in char1:
                char1[i] = 1
            else:
                char1[i] += 1
        for j in word2:
            if j not in char2:
                char2[j] = 1
            else:
                char2[j] += 1
        if len(char1) != len(char2):
            return False
        for i in char1:
            if i not in char2:
                return False
            not_found = True
            for j in char2:
                if char1[i] == char2[j]:
                    not_found = False
                    char2[j] = 0
                    break
            if not_found:
                return False
        for j in char2:
            if char2[j] != 0:
                return False
        return True
