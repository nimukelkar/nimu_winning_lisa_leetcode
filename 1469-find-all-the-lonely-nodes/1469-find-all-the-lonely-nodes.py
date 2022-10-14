# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lonely=[]
    def preorder(self,node):
        if not node:
            return
        if (not node.left and node.right):
            self.lonely.append(node.right.val)
        if (not node.right and node.left):
            self.lonely.append(node.left.val)
        self.preorder(node.left)
        self.preorder(node.right)
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.lonely