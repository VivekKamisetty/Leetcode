#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return
        
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None

            for _ in range(level_size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev.next = None
        
        return root
