from collections import *
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        at={}
        dt={}
        timestamp=[0]
        ans=[True]
        visited={}
        d=defaultdict(list)
        for u,v in prerequisites:
            d[v].append(u)
        print(d)
        
        def dfs(start):
            at[start]=timestamp[0]
            timestamp[0]+=1
            
            #Look for neighbors
            for neighbor in d[start]:
                if neighbor not in visited:
                    visited[neighbor]=visited[start]+1
                    dfs(neighbor)
                else:
                    if neighbor not in dt:
                        ans[0]=False
            
            dt[start]=timestamp[0]
            timestamp[0]+=1
            
        
        for i in d:
            if i in d[i]:
                print("hi")
                return False
        
        for i in range(numCourses):
            if i not in visited:
                visited[i]=0
                dfs(i)
                '''print("Visited=",visited)
                print("Arrival time=",at)
                print("Departure Time=",dt)'''
        return ans[0]
       