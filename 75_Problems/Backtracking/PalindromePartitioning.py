#https://leetcode.com/problems/palindrome-partitioning/
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        avail = []

        def bt(i):
            if len(s) <= i:
                res.append(list(avail))
                return
            
            for j in range(i, len(s)):
                if self.isPalin(s, i , j):
                    avail.append(s[i:j+1])
                    bt(j+1)
                    avail.pop()
        bt(0)
        return res

    def isPalin(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True    
