# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        count=[0]
        if not root:
            return 0
        
        def postorder(node):
            if not node.left and not node.right:
                count[0]=count[0]+1
                return count[0]
            
            if node.left:
                count[0]=postorder(node.left)
            if node.right:
                count[0]=postorder(node.right)
            
            count[0]=count[0]+1
            return count[0]
        ans=postorder(root)
        return ans