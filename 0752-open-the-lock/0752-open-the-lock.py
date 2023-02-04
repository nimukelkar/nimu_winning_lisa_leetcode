from collections import *
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited={}
        
        
        
        
        def calculate(u):
            # Generate valid neighbors of u
            s1=""
            s2=""
            l=[]
            for i in range(len(u)):
                d=(int(u[i])+1)%10
                d2=(int(u[i])-1+10)%10
                s1=u[0:i]+str(d)+u[i+1:]
                s2=u[0:i]+str(d2)+u[i+1:]
                if s1 not in deadends:
                    l.append(s1)
                
                if s2 not in deadends :
                    l.append(s2)
            #print("l=",l)
            return l
        
        
        
        
        
        def bfs(node):
            q=deque()
            q.append(node)
            
            while(q):
                u=q.popleft()
            
                neighborlist=calculate(u)
                
                for neighbor in neighborlist:
                    if neighbor ==target:
                        visited[neighbor]=visited[u]+1
                        return visited[neighbor]
                        
                    if neighbor not in visited:
                        visited[neighbor]=visited[u]+1
                        q.append(neighbor)
            return -1
        
        
        start="0000"
        if start in deadends:
            return -1
        if target in deadends:
            return -1
        if start==target:
            return 0
        visited[start]=0
        return bfs(start)