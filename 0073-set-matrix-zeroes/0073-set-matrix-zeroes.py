class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        x=[]
        y=[]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    x.append(i)
                    y.append(j)
        for i in x:
            for j in range(n):
                grid[i][j]=0
        for j in y:
            for i in range(m):
                grid[i][j]=0
        return grid
        