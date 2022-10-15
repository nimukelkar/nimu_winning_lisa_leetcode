class Solution:
    def __init__(self):
        self.visited=set()
        self.q=[]
        self.levels={}
    def getneighbors(self,start,deadends):
        neighbors=[]
        s1=""
        s2=""
        for i in range(len(start)):
            d=(int(start[i])+1)%10
            d2=(int(start[i])-1+10)%10
            s1=start[0:i]+str(d)+start[i+1:]
            s2=start[0:i]+str(d2)+start[i+1:]
            if s1 not in deadends:
                neighbors.append(s1)
            if s2 not in deadends :
                neighbors.append(s2)
        
        return neighbors
            
    
    def bfs(self,start,target,deadends):
        self.q.append(start)
        self.visited.add(start)
        self.levels[start]=0
        
        
        while(self.q):
            u=self.q.pop(0)
            if u==target:
                return self.levels[u]

            neighbors=self.getneighbors(u,deadends)
           
            for i in neighbors:
                if i not in self.visited:
                    self.visited.add(i)
                    self.q.append(i)
                    self.levels[i]=self.levels[u]+1
        return -1
            
            
        
        
    def openLock(self, deadends: List[str], target: str) -> int:
        start="0000"
        if start in deadends:
            return -1
        count=self.bfs(start,target,deadends)
        return count