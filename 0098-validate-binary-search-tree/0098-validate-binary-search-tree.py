# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        flag=[True]
         
        def dfs(node,min,max):
            if not node.left and not node.right:
                if node.val<=min or node.val>=max:
                    flag[0]=False
            if node.val<=min or node.val>=max:
                    flag[0]=False
            if node.left:
                dfs(node.left,min,node.val)
            if node.right:
                dfs(node.right,node.val,max)
        min=float("-inf")
        max=float("inf")
        dfs(root,min,max)
        return flag[0]
            