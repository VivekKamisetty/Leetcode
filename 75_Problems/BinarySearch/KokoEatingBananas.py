#https://leetcode.com/problems/koko-eating-bananas/description/

import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        res = right 

        while left <= right:
            hours = 0
            mid = (left + right) // 2
            for p in piles:
                hours += ceil(p / mid)
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
