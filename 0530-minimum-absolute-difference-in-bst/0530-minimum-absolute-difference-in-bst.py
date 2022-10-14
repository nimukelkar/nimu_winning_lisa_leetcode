# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l=[]
    def inorder(self,node):
        if not node:
            return
        
        self.inorder(node.left)
        self.l.append(node.val)
        self.inorder(node.right)
    
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        mini=10000
        k=self.l[0]
        l=len(self.l)
        for i in range(1,l):
            if self.l[i]!=self.l[i-1]:
                mini=min(mini,abs(self.l[i]-self.l[i-1]))
        return mini
            
        