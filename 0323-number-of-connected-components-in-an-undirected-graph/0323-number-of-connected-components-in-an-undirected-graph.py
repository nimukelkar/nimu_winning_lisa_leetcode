from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(list)
        visited={}
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        #print("d=",d)
        def dfs(i):
            
            for neighbor in d[i]:
                if neighbor not in visited:
                    visited[neighbor]=visited[i]+1
                    dfs(neighbor)
        
        
        
        
        
        
        
        
        
        
        
        count=0
        for i in range(n):
            if i not in visited:
                visited[i]=0
                dfs(i)
                count+=1
        return count
            
        
        
        
        
        
        