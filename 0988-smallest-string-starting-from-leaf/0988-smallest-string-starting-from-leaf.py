# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        d={
            0:'a',
            1:'b',
            2:'c',
            3:'d',
            4:'e',
            5:'f',
            6:'g',
            7:'h',
            8:'i',
            9:'j',
            10:'k',
            11:'l',
            12:'m',
            13:'n',
            14:'o',
            15:'p',
            16:'q',
            17:'r',
            18:'s',
            19:'t',
            20:'u',
            21:'v',
            22:'w',
            23:'x',
            24:'y',
            25:'z'
        }
        s=""
        l=[]
        
        def dfs(node,s):
            if not node:
                return
            if not node.left and not node.right:
                s+=str(d[node.val])
                l.append((s)[::-1])
                return
            s+=str(d[node.val])
            dfs(node.left,s)
            dfs(node.right,s)
        dfs(root,"")
        print(l)
        return min(l)
        
        
        
        
        
        
        
        