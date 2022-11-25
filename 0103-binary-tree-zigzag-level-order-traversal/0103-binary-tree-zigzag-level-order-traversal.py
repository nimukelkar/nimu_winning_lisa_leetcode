# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        ans=[]
        def bfs(root):
            q=deque()
            q.append(root)
            
            level=0
            while(q):
                temp=[]
                
                for i in range(len(q)):
                    u=q.popleft()
                    temp.append(u.val)
                    
                    if u.left:
                        q.append(u.left)
                    if u.right:
                        q.append(u.right)
                    
                if level%2==0:
                    ans.append(temp)
                else:
                    ans.append(temp[::-1])
                level+=1
        bfs(root)
        return ans
                    
                    