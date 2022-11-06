class Solution:
    def climbStairs(self, n: int) -> int:
        table=[0]*(n+1)

        for i in range(1,n+1):
            if i==1:
                table[i]=1
            elif i==2:
                table[i]=2
            
            else:
                table[i]=table[i-1]+table[i-2]
        return table[n]
        