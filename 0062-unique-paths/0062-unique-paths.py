class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table=[[0 for i in range(n)]for j in range(m)]
        #print(table)
        for i in range(m):
            table[i][0]=1
        
        for j in range(n):
            table[0][j]=1
        #print(table)
        
        for i in range(1,m):
            for j in range(1,n):
                table[i][j]=table[i-1][j]+table[i][j-1]
        return table[m-1][n-1]