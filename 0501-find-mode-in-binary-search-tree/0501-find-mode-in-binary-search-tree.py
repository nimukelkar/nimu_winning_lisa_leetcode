# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d={}
    def preorder(self,node):
        if not node:
            return
        if node.val in self.d:
            self.d[node.val]+=1
        else:
            self.d[node.val]=1
        self.preorder(node.left)
        self.preorder(node.right)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        element=[]
        self.preorder(root)
        max=0
        print("self.d=",self.d)
        self.d=dict(sorted(self.d.items(),key=lambda x:x[1],reverse=True))
        for i in self.d:
            if (self.d[i])>=max:
                max=self.d[i]
                element.append(i)
        return element