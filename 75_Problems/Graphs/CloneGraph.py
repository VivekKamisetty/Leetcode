#https://leetcode.com/problems/clone-graph/description/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        oldToNew = {}

        if node is None:
            return None

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
        
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy_nei = dfs(nei)
                copy.neighbors.append(copy_nei)
        
            return copy
        return dfs(node)
            
        
        
