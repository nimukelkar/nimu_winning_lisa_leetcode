# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        if not root:
            return
        
        def dfs(node,slate):
            if not node.left and not node.right:
                slate.append(node.val)
                if sum(slate)==targetSum:
                    ans.append(slate.copy())
                slate.pop()
                return
            
            slate.append(node.val)
            if node.left:
                dfs(node.left,slate)
            if node.right:
                dfs(node.right,slate)
            slate.pop()
        
        dfs(root,[])
        return ans