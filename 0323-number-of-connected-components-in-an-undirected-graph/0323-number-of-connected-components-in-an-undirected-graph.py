from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d=defaultdict(list)
        visited={}
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        
        def bfs(node):
            q=deque()
            q.append(node)
            
            while(q):
                u=q.popleft()
                for neighbor in d[u]:
                    if neighbor not in visited:
                        visited[neighbor]=visited[u]+1
                        q.append(neighbor)
        
        count=0
        for i in range(n):
            if i not in visited:
                visited[i]=0
                bfs(i)
                count+=1
        return count
                        
                        
        
        
        
        
        
        
        
        
        