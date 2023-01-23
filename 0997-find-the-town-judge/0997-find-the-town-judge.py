from collections import *
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust==[] and n==1:
            return 1
        d1=defaultdict(int)
        d2=defaultdict(int)
        
        for u,v in trust:
            d1[u]+=1
            d2[v]+=1
        #print("d1=",d1)
        #print("d2=",d2)
        
        for i in d2:
            if d2[i]==n-1 and i not in d1:
                return i
        return -1