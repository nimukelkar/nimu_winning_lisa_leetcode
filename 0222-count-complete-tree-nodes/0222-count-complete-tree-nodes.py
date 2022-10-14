# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count=0
    def preorder(self,node):
        if not node:
            return
        self.count+=1
        self.preorder(node.left)
        self.preorder(node.right)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.preorder(root)
        return self.count
        