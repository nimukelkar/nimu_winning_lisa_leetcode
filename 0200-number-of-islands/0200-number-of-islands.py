from collections import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited={}
        
        def getneighbor(node):
            l=[]
            ux,uy=node
            if ux+1<m and grid[ux+1][uy]=="1":
                l.append((ux+1,uy))
            if uy+1<n and grid[ux][uy+1]=="1":
                l.append((ux,uy+1))
            if ux-1>=0 and grid[ux-1][uy]=="1":
                l.append((ux-1,uy))
            if uy-1>=0  and grid[ux][uy-1]=="1":
                l.append((ux,uy-1))
            
            
            return l
            
            
        def bfs(start):
            i,j=start
            q=deque()
            q.append((i,j))
            while(q):
                ux,uy=q.popleft()
                neighborslist=getneighbor((ux,uy))
                #print(neighborslist)
                for neighbor in neighborslist:
                    nx,ny=neighbor
                    if neighbor not in visited:
                        visited[neighbor]=visited[(ux,uy)]+1
                        q.append((nx,ny))
        
                                
        
        
        count=0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=="1":
                    visited[(i,j)]=0
                    bfs((i,j))
                    #print("visited=",visited)
                    count+=1
        
        return count
                    
                