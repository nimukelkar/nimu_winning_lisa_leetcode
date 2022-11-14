# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        
        
        if not root:
            return 0
        
        def dfs(node,count):
            if not node.left and not node.right:
                maxi[0]=max(maxi[0],count)
                return
           
            
            if node.left:
                #count+=1
                dfs(node.left,count+1)
            if node.right:
                #count+=1
                dfs(node.right,count+1)
            
        count=0
        dfs(root,count)
        return maxi[0]+1
            
            