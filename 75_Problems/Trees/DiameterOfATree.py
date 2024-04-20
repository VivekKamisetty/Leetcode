#https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diam = [0]

        def dfs(root):
            if root is None:
                return -1
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            print("Node:", root.val, "Left Height:", left_height, "Right Height:", right_height)
            
            diam[0] = max(diam[0], left_height + right_height + 2)
            
            return 1 + max(left_height, right_height)

        dfs(root)
        return diam[0]
