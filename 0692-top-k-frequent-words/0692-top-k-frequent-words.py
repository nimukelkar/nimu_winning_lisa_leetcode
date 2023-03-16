from heapq import *
from collections import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=defaultdict(int)
        l=[]
        for i in words:
            d[i]+=1
        
        #print(d)
        #Use a priority queue
        d=sorted(d.items(),key=lambda x:(-x[1],x[0]))
        
        for i in range(k):
            l.append(d[i][0])
        return l
        
            