from collections import *
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d=defaultdict(int)
        
        for i in nums:
            d[i]+=1
        
        
        for i in d:
            if d[i]==1:
                return i