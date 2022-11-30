from collections import *
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       
        visited={}
        parent={}
    
        ans=[True]
        def bfs(node):
            q=deque()
            q.append(node)
            
            while(q):
                u=q.popleft()
                
                for neighbor in graph[u]:
                    if neighbor not in visited:
                        visited[neighbor]=(visited[u]+1)%2
                        parent[neighbor]=u
                        q.append(neighbor)
                    else:
                        if parent[u]!=neighbor and visited[neighbor]==visited[u]:
                            ans[0]=False
                            return
                        
        for i in range(len(graph)):
            if i not in visited:
                visited[i]=0
                parent[i]=0
                bfs(i)
        return ans[0]
            
                      
                    