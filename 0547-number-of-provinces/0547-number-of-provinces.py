from collections import *

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        d=defaultdict(list)
        n=len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    d[i].append(j)
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
                        
        