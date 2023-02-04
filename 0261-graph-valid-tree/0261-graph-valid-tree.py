from collections import *
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #No of connected components=1
        #No cycles
        visited=set()
        flag=[True]
        parents={}
        d=defaultdict(list)
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
                        parents[neighbor]=u
                        q.append(neighbor)
                    else:
                        if parents[u]!=neighbor:
                            flag[0]=[False]
        count=0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                bfs(i)
                count+=1
        if count==1 and flag[0]==True:
            return True
        return False
                
                            
                        
        