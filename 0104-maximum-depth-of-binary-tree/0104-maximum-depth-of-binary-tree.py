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
        
        def dfs(node,depth):
            if not node.left and not node.right:
                depth+=1
                maxi[0]=max(maxi[0],depth)
                return
            
            if node.left:
                dfs(node.left,depth+1)
            if node.right:
                dfs(node.right,depth+1)
        dfs(root,0)
        return maxi[0]