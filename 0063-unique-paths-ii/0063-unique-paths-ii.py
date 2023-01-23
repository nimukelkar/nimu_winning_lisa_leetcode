class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        #Base cases
        
        if grid[m-1][n-1]==1:
            return 0
        if grid[0][0]==1:
            return 0
        if len(grid)==1 and grid[0][0]==0 and grid[m-1][n-1]==0:
            return 1
        table=[[0 for i in range(n)]for j in range(m)]
        #print(table)
        
        for i in range(1,m):
            if grid[i][0]==0:
                table[i][0]=1
            else:
                break
        
        for j in range(1,n):
            if grid[0][j]==0:
                table[0][j]=1
            else:
                break
        #print(table)
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==0:
                    table[i][j]=table[i-1][j]+table[i][j-1]
        #print(table)
        return table[m-1][n-1]