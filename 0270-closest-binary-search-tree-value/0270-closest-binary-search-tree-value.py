# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diff=100000000
        self.min_value=0
    
    def preorder(self,node,target):
        if not node:
            return
        if abs(target-node.val)<self.diff:
            self.diff=abs(target-node.val)
            self.min_value=node.val
        self.preorder(node.left,target)
        self.preorder(node.right,target)
        
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.preorder(root,target)
        return self.min_value