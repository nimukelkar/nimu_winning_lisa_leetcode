from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d=defaultdict(list)
        visited=set()
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        def bfs(start):
            q=deque()
            q.append(start)
            
            while(q):
                u=q.popleft()
                
                for neighbor in d[u]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        if not edges:
            return True
        bfs(source)
        
        if destination not in visited:
            return False
        return True
        
        
        