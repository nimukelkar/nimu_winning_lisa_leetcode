class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #Next greatest element with slight variation.
        d2={}
        for i in range(len(heights)):
            d2[heights[i]]=i
        #print("d2=",d2)
        
        stk=[]
        d={}
        ans=[]
        
        for i in range(len(heights)):
            
            while(stk and heights[i]>=stk[-1]):
                d[stk[-1]]=heights[i]
                stk.pop()
            
            stk.append(heights[i])
        
        
        while(stk):
            d[stk[-1]]=-1
            ans.append(d2[stk[-1]])
            stk.pop()
        
        return sorted(ans)
        