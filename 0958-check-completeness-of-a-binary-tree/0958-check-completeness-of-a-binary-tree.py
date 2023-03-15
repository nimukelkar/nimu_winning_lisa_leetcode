# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # ADd nodes in deque in bfs way
        if not root:
            return True
        nullNodeFound=False
        q=deque()
        q.append(root)
        while(q):
            node=q.popleft()
            if not node:
                nullNodeFound=True
            
            else:
                if nullNodeFound==True:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
        