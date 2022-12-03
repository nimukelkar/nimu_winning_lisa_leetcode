from collections import *
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=defaultdict(int)
        l=[]
        
        for i in nums:
            d[i]+=1
        
        d=dict(sorted(d.items(),key=lambda x:[x[1],-x[0]]))
        #print(d)
        
        for i in d:
            for j in range(d[i]):
                l.append(i)
        return l