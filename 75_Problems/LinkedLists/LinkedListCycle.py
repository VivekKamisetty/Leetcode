#https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """nextList = []
        temp = head

        if temp == None:
            return False

        while (temp.next != None):
            if temp.next in nextList:
                return True
            nextList.append(temp.next)
            temp = temp.next
        return False"""
        
        if head == None:
            return False
            
        slow = head
        fast = head.next

        while(fast is not None and fast.next is not None):
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
            
