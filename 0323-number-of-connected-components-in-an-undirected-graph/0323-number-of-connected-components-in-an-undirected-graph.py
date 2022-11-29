from collections import *
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(list)
       
        
        visited=set()
        
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        #print(d)
        def bfs(node):
            q=deque()
            q.append(node)
        
            while(q):
                u=q.popleft()
                for neighbor in d[u]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            return
                    
        
        count=0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count+=1
        return count
            
                
                     
                  
        