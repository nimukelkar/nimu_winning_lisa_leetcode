# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import *
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        ans=[]
        def bfs(node):
            q=deque()
            q.append(node)
            while(q):
                temp=[]
                
                for i in range(len(q)):
                    u=q.popleft()
                    temp.append(u.val)
                    
                    if u.left:
                        q.append(u.left)
                    if u.right:
                        q.append(u.right)
                ans.append(temp)
        bfs(root)
        return ans
                    
            