class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+","-","*","/"])
        result = []
        for i in tokens:
            if i not in ops:
                result.append(int(i))
            else:
                two = result.pop()
                one = result.pop()
                if i == "+":
                    result.append(one+two)
                elif i == "-":
                    result.append(one-two)
                elif i == "*":
                    result.append(one*two)
                else:
                    result.append(int(one/two))
        return result[0]
