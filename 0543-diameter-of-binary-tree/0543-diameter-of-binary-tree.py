# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        
        def dfs(node):
            if not node.left and not node.right:
                return 1
            hl,hr=0,0
            if node.left:
                hl=dfs(node.left)
            if node.right:
                hr=dfs(node.right)
            
            h=max(hl,hr)+1
            maxi[0]=max(maxi[0],hl+hr)
            return h
        
        dfs(root)
        return maxi[0]
        
    