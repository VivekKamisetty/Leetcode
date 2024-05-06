#https://leetcode.com/problems/car-fleet/

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            time_to_target = round((target - p) / float(s), 6)
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
        return len(stack)
