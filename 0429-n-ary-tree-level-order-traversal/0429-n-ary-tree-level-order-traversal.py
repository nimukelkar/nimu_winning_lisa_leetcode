"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        ans=[]
        
        def bfs(root):
            q=deque()
            q.append(root)
            
            
            while(q):
                
                temp=[]
                for i in range(len(q)):
                    u=q.popleft()
                    temp.append(u.val)
                    
                    for child in u.children:
                        q.append(child)
                ans.append(temp)
        bfs(root)
        return ans
                