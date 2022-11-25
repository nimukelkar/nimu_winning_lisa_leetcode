# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        if not root:
            return
        
        def bfs(root):
            q=deque()
            q.append(root)
            
            while(q):
                temp=[]
                for i in range(len(q)):
                    u=q.popleft()
                    temp.append(u.val)
                    
                    if u.left:
                        q.append(u.left)
                    
                    if u.right:
                        q.append(u.right)
                avg=sum(temp)/len(temp)
                ans.append(avg)
        bfs(root)
        return ans
                    