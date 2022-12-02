from collections import *
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d=defaultdict(list)
        visited={}
        parents={}
        ans=[True]
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        #No of connected components=1 and no cycles
        
        def dfs(node):
            for neighbor in d[node]:
                if neighbor not in visited:
                    visited[neighbor]=visited[node]+1
                    parents[neighbor]=node
                    dfs(neighbor)
                
                else:
                    # Check for cycles
                    if parents[node]!=neighbor:
                        ans[0]=False
                        
        
        
        
        
        
        
        
        
        count=0
        for i in range(n):
            if i not in visited:
                visited[i]=0
                parents[i]=0
                dfs(i)
                count+=1
        if count>1:
            ans[0]=False
        return ans[0]
                