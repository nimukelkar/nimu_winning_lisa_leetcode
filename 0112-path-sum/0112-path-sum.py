# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        slate=[]
        self.flag=False

        if not root:
            return self.flag
        def dfs(node):
            if not node.left and not node.right:
                slate.append(node.val)
                if sum(slate)==targetSum:
                    self.flag=True
                
                slate.pop()
                return
            slate.append(node.val)
            if  node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            slate.pop()
        dfs(root)
        return self.flag
            
            
                