class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #BFS function
        #No of times this function is called.
        visited=set()
        d=defaultdict(list)
        
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
                        visited.add(neighbor)
                        q.append(neighbor)
        
        
        
        
        
        
        
        
        
        
        
        count=0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                bfs(i)
                count+=1
        return count