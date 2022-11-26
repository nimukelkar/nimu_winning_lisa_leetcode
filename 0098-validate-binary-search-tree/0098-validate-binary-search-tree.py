# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        if not root:
            return False
        def dfs(node):
            if not node.left and not node.right:
                ans.append(node.val)
                return
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        print(ans)
        for i in range(len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False
        return True