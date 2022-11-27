# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=[0]
        def postorder(node):
            if not node.left and not node.right:
                ans[0]+=1
                return[node.val,1]
            sum_l,count_l,sum_r,count_r=0,0,0,0
            if node.left:
                sum_l,count_l=postorder(node.left)
            if node.right:
                sum_r,count_r=postorder(node.right)
            count_tot=count_l+count_r+1
            sum_tot=sum_l+sum_r+node.val
            #print("sum_tot=",sum_tot)
            #print("count_tot=",count_tot)
            if sum_tot//count_tot==node.val:
                ans[0]+=1
            return[sum_tot,count_tot]
        
        
        l=postorder(root)
        #print(l)
        return ans[0]
                
            
                