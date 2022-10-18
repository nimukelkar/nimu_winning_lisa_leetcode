class Solution:
    def __init__(self):
        self.time=0
        self.q=[]
       
        self.levels={}
        self.max_value=0
    def getneighbor(self,u,manager,informTime):
        neighbor=[]
        for i in range(len(manager)):
            if manager[i]==u:
                neighbor.append(i)
        #print("neighbor=",neighbor)
        return neighbor
        
    def bfs(self,headID,path,informTime,manager,d):
        self.levels[headID]=0
        self.q.append(headID)
       
        max_value=0
        while(self.q):
            u=self.q.pop(0)
            #print("u=",u)
            
            #neighbor=self.getneighbor(u,manager,informTime)
            if u in d:
                for i in d[u]:
                #print("i=",i)
                #for i in neighbor:
                    
                        #print("i=",i)
                        self.q.append(i)
                        self.levels[i]=self.levels[u]+informTime[u]
                        #print("self.levels=",self.levels)
                        
                        max_value=max(max_value,self.levels[i])    
        return max_value
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        path=0
        d={}
        for i in range(len(manager)):
            if manager[i] in d:
                if manager[i]!=-1:
                    d[manager[i]].append(i)
            else:
                if manager[i]!=-1:
                    d[manager[i]]=[i]
        if d=={}:
            return 0
        #print("d=",d)
        count=self.bfs(headID,path,informTime,manager,d)
        
        #print(self.levels)
        #return max(self.levels.values())
        return count