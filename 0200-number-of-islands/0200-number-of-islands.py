from collections import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Connected components
        visited={}
        
        def getneighbor(node):
            nx,ny=node
            l=[]
            if nx+1<=m-1 and grid[nx+1][ny]=="1":
                l.append((nx+1,ny))
            if ny+1<=n-1 and grid[nx][ny+1]=="1":
                l.append((nx,ny+1))
            if nx-1>=0 and grid[nx-1][ny]=="1":
                l.append((nx-1,ny))
            if ny-1>=0 and grid[nx][ny-1]=="1":
                l.append((nx,ny-1))
                
            return l
        
        
        def dfs(node):
            ux,uy=node
            # Check neighbors of ux,uy
            
            neighborlist=getneighbor(node)
            
            for neighbor in neighborlist:
                if neighbor not in visited:
                    visited[neighbor]=visited[(ux,uy)]+1
                    dfs(neighbor)
        
        
        
        
        
        
        
        
        
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if ((i,j) not in visited and grid[i][j]=="1"):
                    visited[(i,j)]=0
                    dfs((i,j))
                    #print("visited=",visited)
                    count+=1
        return count