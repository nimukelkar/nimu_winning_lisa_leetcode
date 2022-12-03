from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        
        for i in s:
            d[i]+=1
        
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        #print(d)
        s1=""
        for i in d:
            for j in range(d[i]):
                s1+=i
        return s1
                