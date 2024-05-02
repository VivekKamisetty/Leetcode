#https://leetcode.com/problems/min-stack/description/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.mini==None:
            self.mini = val
        if val < self.mini:
            self.mini = val

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if not self.stack:
            self.mini=None
        if val == self.mini:
            self.mini = min(self.stack)
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
