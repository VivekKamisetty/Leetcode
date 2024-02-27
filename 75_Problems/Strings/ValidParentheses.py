#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening_brac = "({["
        closing_brac = ")}]"
        count = 0

        for char in s:
            if char in opening_brac:
                stack.append(char)
            elif char in closing_brac:
                if not stack:
                    return False
                elif (opening_brac.index(stack.pop()) != closing_brac.index(char)):
                    return False

        return len(stack) == 0 
                 
        
