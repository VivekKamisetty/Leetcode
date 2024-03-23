#https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        print(dic)

        heap = [(-freq, num) for num, freq in dic.items()]
        print(heap)
        heapq.heapify(heap)

        top_k = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            top_k.append(num)

        return top_k



        
        


        
