# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        mini=[float("inf")]
        
        if not root:
            return 0
        
        def dfs(node,count):
            if not node.left and not node.right:
            
                mini[0]=min(mini[0],count)
                
                         
                
            if node.left:
                dfs(node.left,count+1)
            if node.right:
                dfs(node.right,count+1)
        count=1
        dfs(root,count)
        return mini[0]
            
                
        