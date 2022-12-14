class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def sub(n):                                  # this recursive function 
            if not n : return 0                      # computes and collects 
            s = n.val + sub(n.left) + sub(n.right)   # sums of all subtrees 
            sums.append(s)
            return s
        
        diff, prod, sums = inf, 0, []
        
        sub(root)
        
        for s in sums:                               # next, we should find the
            if (d:=abs(sums[-1] - 2*s)) < diff:      # product of subtrees with
                diff, prod = d, (sums[-1] - s) * s   # minimal difference of sums
        
        return prod % 1_000_000_007