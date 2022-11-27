# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=[]
        def bfs(node):
            q=deque()
            q.append(node)
            count=1
            
            while(q):
                
                temp=[]
                
                for i in range(len(q)):
                    u=q.popleft()
                    temp.append(u.val)
                    
                    if u.left:
                        q.append(u.left)
                    
                    if u.right:
                        q.append(u.right)
                ans.append((sum(temp),count))
                count+=1
        bfs(root)
        ans=sorted(ans,key=lambda x:x[0],reverse=True)
        #print(ans)
        return ans[0][1]
                           
                
                
                    
            
        