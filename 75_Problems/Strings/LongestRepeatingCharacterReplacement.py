#https://leetcode.com/problems/longest-repeating-character-replacement/description/
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        count = {}
        result = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            
            while (right - left +1) - max(count.values()) > k:
                count[s[left]] -= 1
                left+=1

            result = max(result, right-left+1)
        return result
