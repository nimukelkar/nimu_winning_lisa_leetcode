class Solution:
    def __init__(self):
        self.visited=set()
        self.q=[]
        self.level={}
    
    def getneighbors(self,u,grid):
        m=len(grid)
        n=len(grid[0])
        neighbors=[]
        ux,uy=u[0],u[1]
        
        
        nx=ux
        ny=uy+1
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        nx=ux
        ny=uy-1
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        
        nx=ux+1
        ny=uy
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        
        nx=ux-1
        ny=uy
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        
        nx=ux-1
        ny=uy-1
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        
        nx=ux+1
        ny=uy+1
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        
        nx=ux-1
        ny=uy+1
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        
        
        nx=ux+1
        ny=uy-1
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1 and grid[nx][ny]!=1:
            neighbors.append((nx,ny))
        #print("neighbors=",neighbors)
        return neighbors
    
    
    def bfs(self,start,end,grid):
        self.level[start]=1
        while self.q:
            u=self.q.pop(0)
            if u==end:
                return self.level[u]
            else:
                neighbors=self.getneighbors(u,grid)
                for i in neighbors:
                    if i not in self.visited:
                        self.q.append(i)
                        self.visited.add(i)
                        self.level[i]=self.level[u]+1
        return -1
            
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        start=(0,0)
        if grid[0][0]==1:
            return -1
        end=(m-1,n-1)
        self.visited.add(start)
        self.q.append(start)

        count=self.bfs(start,end,grid)
        return count