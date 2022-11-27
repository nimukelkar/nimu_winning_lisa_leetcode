# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        #count=[0]
        if not root:
            return 0
        
        def postorder(node):
            if not node.left and not node.right:
                return 1
            count_l,count_r=0,0
            if node.left:
                count_l=postorder(node.left)
            if node.right:
                count_r=postorder(node.right)
            
            count=count_l+count_r+1
            return count
        ans=postorder(root)
        return ans