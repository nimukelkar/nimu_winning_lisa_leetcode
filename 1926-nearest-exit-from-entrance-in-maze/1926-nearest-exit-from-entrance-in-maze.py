class Solution:
    def __init__(self):
        self.levels={}
        self.q = []
        self.visited = set()
        
    def getneighbors(self,u,n,maze,start):
        m=len(maze)
        n=len(maze[0])
        neighbors=[]
        ux,uy=u[0],u[1]
        nx=(ux)
        ny=(uy+1)
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1:
            if maze[nx][ny]!="+":
                neighbors.append((nx,ny))
        nx = (ux)
        ny = (uy - 1)
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1:
            if maze[nx][ny]!="+":
                neighbors.append((nx,ny))
        nx = (ux + 1)
        ny = (uy)
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1:
            if maze[nx][ny]!="+":
                neighbors.append((nx,ny))
        nx = (ux-1)
        ny = (uy)
        if nx>=0 and ny>=0 and nx<=m-1 and ny<=n-1:
            if maze[nx][ny]!="+":
                neighbors.append((nx,ny))
        
        #print("neighbors=",neighbors)
        return neighbors
    
    def bfs(self,start,maze):
        self.levels={}
        m=len(maze)
        n=len(maze[0])
        self.levels[start]=0

        self.q.append(start)
        self.visited.add(start)


        while (self.q):

            u = self.q.pop(0)

            ux,uy=u[0],u[1]
           
            if ux==0 or ux==m-1 or uy==0 or uy==n-1:
                if self.levels[u]!=0:
                #if ux!=start[0] and uy!=start[1]:
                    return self.levels[u]
                
            neighbors=self.getneighbors(u,n,maze,start)
            for i in neighbors:

                if i not in self.visited:

                    self.visited.add(i)
                    self.q.append(i)
                    self.levels[i]=self.levels[u]+1
        return -1

       
       
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        
        

        count = self.bfs(tuple(entrance),maze)
        return count