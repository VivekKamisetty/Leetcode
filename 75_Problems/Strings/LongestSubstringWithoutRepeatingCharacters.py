#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        charSet = set()
        maxLength = 0

        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left+=1
                charSet.add(s[right])
        return maxLength

        """maxc = 0
        c = 0
        already_occurred = ""
        for char in s:
            if(char in already_occurred):
                c=1
            else:
                c=c+1
                already_occurred+=char
            if c > maxc:
                maxc = c
            print(c)
        return maxc"""

        """substring = ""
        for char in s:
            if char not in substring:
                substring+=char
        print(substring)
        return len(substring)"""

        
