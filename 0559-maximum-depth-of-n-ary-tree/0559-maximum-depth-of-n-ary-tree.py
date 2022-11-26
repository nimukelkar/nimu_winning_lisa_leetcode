"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        maxi=[0]
        if not root:
            return 0
        
        def dfs(node,depth):
            if not node.children:
                depth+=1
                maxi[0]=max(maxi[0],depth)
                return
            
            for i in node.children:
                dfs(i,depth+1)
        dfs(root,0)
        return maxi[0]
                