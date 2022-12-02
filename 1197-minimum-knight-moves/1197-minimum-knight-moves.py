from collections import *
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x==0 and y==0:
            return 0
        x=abs(x)
        y=abs(y)
        ans=[]
        visited={}
    
        def getneighbor(node):
            
            ux,uy=node
            l=[]
            l.append((ux+1,uy+2))
            l.append((ux+2,uy+1))
            
            l.append((ux-1,uy+2))
            l.append((ux+2,uy-1))
            
            l.append((ux-2,uy+1))
            l.append((ux+1,uy-2))
            
            l.append((ux-2,uy-1))
            l.append((ux-1,uy-2))
            #print("l=",l)
            
            return l

            
        def bfs(node):
            nx,ny=node
            
            q=deque()
            q.append((nx,ny))
            
            while(q):
                ux,uy=q.popleft()
                if ux<-1 or uy<-1:
                    continue
              
                neighborlist=getneighbor((ux,uy))
                if (x,y) in neighborlist:
                    return visited[(ux,uy)]+1
                    
                
                for neighbor in neighborlist:
                    
                    if neighbor not in visited:
                        visited[neighbor]=visited[(ux,uy)]+1   
                        q.append(neighbor)
                    
        
        
        
        
        visited[(0,0)]=0
        ans=bfs((0,0))  
        return ans
                   
        
                