# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans=[0]
        def dfs(node):
            if not node.left and not node.right:
                return 1
            
            h_l,h_r=0,0
            if node.left:
                h_l=dfs(node.left)
            if node.right:
                h_r=dfs(node.right)
            
            max_ht=max(h_l,h_r)+1
            ans[0]=max(ans[0],h_l+h_r)
            return max_ht
        dfs(root)
        return ans[0]
            