#https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if head is None or head.next is None or head.next.next is None:
            return head

        slow = head
        fast = head.next

        while(fast is not None):
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                break
        
        mid = slow
        right_head = mid.next
        mid.next = None

        one = right_head
        two = one.next
        
        one.next = None

        while(two is not None):
            temp = two.next
            two.next = one
            one = two
            two = temp
        rev = one
        
        temp = head
        dummy = ListNode(-1)
        current = dummy
        count = 0

        while temp is not None and rev is not None:
            if count%2 == 0:
                dummy.next = temp
                temp = temp.next
            else:
                dummy.next = rev
                rev = rev.next
            dummy = dummy.next
            count+=1

        if temp is not None:
            dummy.next = temp
        elif rev is not None:
            dummy.next = rev
        
