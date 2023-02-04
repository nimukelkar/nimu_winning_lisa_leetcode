# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        ans=[False]
        def dfs(node,slate):
            if not node.left and not node.right:
                slate.append(node.val)
                if sum(slate)==targetSum:
                    ans[0]=[True]  
                slate.pop()
                return
            
            slate.append(node.val)
            if node.left:
                dfs(node.left,slate)
            if node.right:
                dfs(node.right,slate)
            slate.pop()
        dfs(root,[])
        return ans[0]