from collections import *
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        flag=True
        for i in arr:
            d[i]+=1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        #print(d)
        l=[]
        for i in d:
            l.append(d[i])
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                flag=False
        return flag
            