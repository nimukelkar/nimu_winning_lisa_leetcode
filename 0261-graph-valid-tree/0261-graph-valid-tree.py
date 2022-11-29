from collections import *
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A graph is a valid tree if connected components=1 
        # A graph is a valid tree if no of cycles=0
        d=defaultdict(list)
        visited=set()
        parents={}
        parents[0]=0
        flag=[True]
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        print(d)
        
        def bfs(node):
            q=deque()
            q.append(node)
            visited.add(node)
            #parents[node]=-1
            
            while(q):
                u=q.popleft()
                
                for neighbor in d[u]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parents[neighbor]=u
                        q.append(neighbor)
                    
                    else:
                        #print("In here")
                        if neighbor in visited and parents[u]!=neighbor:
                            flag[0]=False
        count=0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count+=1
        #print("visited=",visited)
        #print("parents=",parents)
        #print(count)
        if count>1:
            flag[0]=False
        return flag[0]
                            
        
        
        
        
        
            
            
       