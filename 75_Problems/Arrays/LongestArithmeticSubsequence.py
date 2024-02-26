#https://leetcode.com/problems/longest-arithmetic-subsequence/description/

class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """freq_dict = {}
        maxFreq = 0
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = abs(nums[i] - nums[j])
                freq_dict[diff] = freq_dict.get(diff, 0) + 1
                maxFreq = max(maxFreq, freq_dict[diff])

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == maxFreq:
                    count+=1
                    print(nums[i], nums[j])

        return count"""

        d = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = nums[j] - nums[i]
                d[j, diff] = d.get((i, diff), 1) + 1
        
        return max(d.values())
