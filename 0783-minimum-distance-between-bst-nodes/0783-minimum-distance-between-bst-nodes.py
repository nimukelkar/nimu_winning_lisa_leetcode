# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        l=[]
        
        def inorder(node):
            if not node.left and not node.right:
                l.append(node.val)
                return
            
            if node.left:
                inorder(node.left)
            l.append(node.val)
            if node.right:
                inorder(node.right)
        
        inorder(root)
        print(l)
        diff=float("inf")
        for i in range(len(l)-1):
            diff=min(l[i+1]-l[i],diff)
        return diff
            