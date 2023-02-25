# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        if root.left:
            self.leftNode(root.left,res)
        if root.left or root.right:
            self.leafNode(root,res)
        if root.right:
            self.rightNode(root.right,res)
        return res
        
    def leftNode(self,root,res):                  #pre-order
        if not root:
            return
        if root.left:                             
            res.append(root.val)
            self.leftNode(root.left,res)
        elif root.right:
            res.append(root.val)
            self.leftNode(root.right,res)
        # print("left",res)
        return res
    
    
    def rightNode(self,root,res):                 #post-order
        if not root:
            return
        if root.right:                              
            self.rightNode(root.right,res)
            res.append(root.val)
        elif root.left:
            self.rightNode(root.left,res)
            res.append(root.val)
        # print("right",res)
        return res
    
    
    def leafNode(self,root,res):
        if not root:
            return
        if not root.right and not root.left:
            res.append(root.val)
        self.leafNode(root.left,res)
        self.leafNode(root.right,res)
        # print("leaf",res)
        return res