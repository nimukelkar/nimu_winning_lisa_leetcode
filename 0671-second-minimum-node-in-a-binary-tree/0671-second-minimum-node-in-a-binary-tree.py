# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l=[]
    def preorder(self,node):
        if not node:
            return
        self.l.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.preorder(root)
        self.l=sorted(self.l)
        print(self.l)
        m=min(self.l)
        
        for i in self.l:
            if i>m:
                return i
        return -1