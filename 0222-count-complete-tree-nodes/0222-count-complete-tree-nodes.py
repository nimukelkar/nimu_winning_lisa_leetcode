# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans=[0]
    
        if not root:
            return 0
        def dfs(node):
            if not node.left and not node.right:
                ans[0]+=1
                return
            ans[0]+=1    
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
    
        dfs(root)
        return ans[0]