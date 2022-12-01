# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return 
        def dfs(node):
            if not root.left and not root.right:
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            temp=node.left
            node.left=node.right
            node.right=temp
        
        dfs(root)
        return root