# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        mini=[10000000000]
        if not root:
            return 0
        def dfs(node,depth):
            if not node.left and not node.right:
                depth+=1
                mini[0]=min(depth,mini[0])
                return
            
            if node.left:
                dfs(node.left,depth+1)
            if node.right:
                dfs(node.right,depth+1)
        
        dfs(root,0)
        return mini[0]
            
            