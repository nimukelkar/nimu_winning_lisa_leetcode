class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        visited={}
        
        
        
        
        
       
        
        
        
        
        
        
        
        
        
        def getneighbor(node):
            nx,ny=node
            l=[]
            if nx+1<m and grid[nx+1][ny]=="1":
                l.append((nx+1,ny))
            if ny+1<n and grid[nx][ny+1]=="1":
                l.append((nx,ny+1))
            if nx-1>=0 and grid[nx-1][ny]=="1":
                l.append((nx-1,ny))
            if ny-1>=0 and grid[nx][ny-1]=="1":
                l.append((nx,ny-1))
            return l
            
            
        
        
        def dfs(node):
            neighborlist=getneighbor(node)
            for neighbor in neighborlist:
                if neighbor not in visited:
                    visited[neighbor]=node
                    dfs(neighbor)
            
        
        
        m,n=len(grid),len(grid[0])
        count=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    visited[(i,j)]=0
                    dfs((i,j))
                    count+=1
        return count