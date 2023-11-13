class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        slist = list(s)
        vlist = list()
        for i in range(len(slist)):
            if slist[i] in vowels:
                vlist.append(slist[i])
                slist[i] = None
        vlist.sort()
        vlist.reverse()
        result = ""
        for i in slist:
            if i == None:
                result = result + vlist.pop()
            else:
                result = result + i
        return result
