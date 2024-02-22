#https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1

        for i in range (len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        if count_s == count_t:
            return True
        else:
            return False
        
