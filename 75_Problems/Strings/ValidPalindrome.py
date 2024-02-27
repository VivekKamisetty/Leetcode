#https://leetcode.com/problems/valid-palindrome/

import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        neSp = s.replace(' ', '')
        naSp = neSp.lower()
        noSp = re.sub('[^a-zA-Z0-9]','',naSp)
        print(noSp)
        print(noSp[::-1])
        if noSp == noSp[::-1]:
            return True
        
