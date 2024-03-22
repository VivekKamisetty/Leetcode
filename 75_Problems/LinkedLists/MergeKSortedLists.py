#https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, head))
        
        dummy = ListNode(-1)
        current = dummy

        while min_heap:
            val, node = heappop(min_heap)
            
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        
        return dummy.next
        
                

