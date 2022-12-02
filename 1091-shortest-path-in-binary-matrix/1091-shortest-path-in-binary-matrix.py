from collections import *
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        def getneighbor(u):
            neighbors=[]
            ux,uy=u
            nx=ux
            ny=uy+1
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux+1
            ny=uy
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux+1
            ny=uy+1
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux-1
            ny=uy-1
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux+1
            ny=uy-1
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux-1
            ny=uy+1
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux
            ny=uy-1
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            
            nx=ux-1
            ny=uy
            if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
                neighbors.append((nx,ny))
            #print("neighbors=",neighbors)
            return neighbors
                
        
        
        
        def bfs(start):
            nx,ny=start
            q=deque()
            q.append(start)
            
            while(q):
                u=q.popleft()
                #print("u=",u)
                neighborlist=getneighbor(u)
               
                for neighbor in neighborlist:
                    if neighbor==target:
                        visited[neighbor]=visited[u]+1
                        return visited[neighbor]
                    if neighbor not in visited:
                        visited[neighbor]=visited[u]+1
                        q.append(neighbor)
            return -1
        
        
        
        
       
        n,m=len(grid),len(grid[0])
        target=(m-1,n-1)
        visited={}
        start=(0,0)
        if grid[0][0]==1:
            return -1
        if grid[0][0]==0 and n==1:
            return 1
        visited[start]=1
        ans=bfs(start)
        return ans
        