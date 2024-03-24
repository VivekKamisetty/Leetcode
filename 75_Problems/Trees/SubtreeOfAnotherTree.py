#https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def isSameTree(p, q):

            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif (p.val != q.val):
                return False

            left_same = isSameTree(p.left, q.left)
            right_same = isSameTree(p.right, q.right)


            return left_same and right_same

        if root is None and subRoot is None:
            return True

        if root is None:
            return False
        
        if root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        


        
