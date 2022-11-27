# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        
        if not root:
            return 0
        
        def postorder(node):
            if not node.left and not node.right:
                return 1
            h_l,h_r=0,0
            if node.left:
                h_l=postorder(node.left)
            if node.right:
                h_r=postorder(node.right)
            print("height_left=",h_l)
            print("height_right=",h_r)
            
            height=max(h_l,h_r)+1
            maxi[0]=max(maxi[0],h_l+h_r)
            return height
        
        postorder(root)
        return maxi[0]