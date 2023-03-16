# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        root=TreeNode(postorder.pop())
        k=inorder.index(root.val)
        left_in,right_in=inorder[:k],inorder[k+1:]
        left_post,right_post=[],[]
        sri=set(right_in)
        while postorder:
            i=postorder.pop()
            if i in sri:
                right_post.append(i)
            else:
                left_post.append(i)
                break
        left_post=postorder+left_post
        right_post.reverse()
        
        root.left=self.buildTree(left_in,left_post)
        root.right=self.buildTree(right_in,right_post)
        
        return root