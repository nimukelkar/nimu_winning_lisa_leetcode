# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum=0
    def preorder(self,node,low,high):
        if not node:
            return
        if node.val>=low and node.val<=high:
            self.sum+=node.val
        self.preorder(node.left,low,high)
        self.preorder(node.right,low,high)
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.preorder(root,low,high)
        return self.sum