#https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    counter = 1
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0


        def dfs(root):
            if root is None:
                return
            if root.left:
                if root.val <= root.left.val:
                    self.counter += 1
                else:
                    root.left.val = root.val
            if root.right:    
                if root.val <= root.right.val:
                    self.counter += 1
                else:
                    root.right.val = root.val
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.counter
            

