#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = "+-*/"
        stack = []
        res = 1

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == "+":
                    res = a + b
                elif tokens[i] == "-":
                    res = (b - a)
                elif tokens[i] == "/":
                    res = (float(b) / a)
                elif tokens[i] == "*":
                    res = (b*a)
                stack.append(int(res))
        return int(stack[0])
                
