https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                print("append", curr)
                print("\n")
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print("curr", curr)
            count+=1

            if count == k:
                return curr.val
            curr = curr.right
        return None
