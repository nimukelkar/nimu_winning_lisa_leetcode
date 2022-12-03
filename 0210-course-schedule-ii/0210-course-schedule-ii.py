from collections import *
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        
        for u,v in prerequisites:
            d[v].append(u)
        #print(d)
        flag=[True]
        l=[]
        
        def dfs(node):
            at[node]=timestamp[0]
            timestamp[0]+=1
            
            for neighbor in d[node]:
                if neighbor not in visited:
                    visited[neighbor]=visited[node]+1
                    dfs(neighbor)
                else:
                    if neighbor not in dt:
                        flag[0]=False
            dt[node]=timestamp[0]
            timestamp[0]+=1
            l.append(node)
            
        
        
        
        
        visited={}
        at={}
        dt={}
        timestamp=[0]
        for i in range(numCourses):
            if i not in visited:
                visited[i]=0
                dfs(i)
        if flag[0]==True:
            return l[::-1]
        else:
            return []