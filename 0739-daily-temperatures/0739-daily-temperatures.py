from collections import *
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        ans=[0 for i in range(len(temperatures))]
        # Use a monotonic stack
        
        stk=[]
        
        
        for i in range(len(temperatures)):
            
            while(stk and temperatures[i]>temperatures[stk[-1]]):
            
                idx=stk.pop()
                ans[idx]=i-idx
               
            
            
            stk.append(i)
        return ans
        
        
        
        
        
      
      