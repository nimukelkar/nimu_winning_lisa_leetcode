# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        ans=[True]
        def dfs(node,min,max):
            if not node.left and not node.right:
                if node.val<=min or node.val>=max:
                    ans[0]=False
                    return
            if node.val<=min or node.val>=max:
                ans[0]=False
            if node.left:
                dfs(node.left,min,node.val)
            if node.right:
                dfs(node.right,node.val,max)
            
                    
        
        
        
        
        
    
        min=float("-inf")
        max=float("inf")
        dfs(root,min,max)
        return ans[0]