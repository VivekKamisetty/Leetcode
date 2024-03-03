#https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=daily-question&envId=2024-03-03

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        count = 0

        while (temp != None):
           temp = temp.next
           count +=1
        
        if count == 0:
            return head.next

        if count == n:
            return head.next

        temp = head
        for i in range((count - n - 1)):
            temp = temp.next
        
        temp.next = temp.next.next

        #if temp.next is not None:
        #    temp.next = temp.next.next

        return head
