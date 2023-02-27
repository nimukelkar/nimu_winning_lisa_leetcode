class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk=[]
        n=len(heights)
        final=[0 for i in range(n)]
        rspan=[0 for i in range(n)]
        ans=[0 for i in range(n)]
        idx_left=[0 for i in range(n)]
        right_result=[1 for i in range(len(heights))]
        left_result=[1 for i in range(len(heights))]
        
        #Find next smaller element
        for i in range(n):
            
            
            while(stk and heights[i]<heights[stk[-1]]):
                idx=stk.pop()
                ans[idx]=i-idx
            stk.append(i)
            
        
        
        for i in range(n):
            if ans[i]==0:
                rspan[i]=n-i
            else:
                rspan[i]=ans[i]
      
        for i in range(n):
            right_result[i]=rspan[i]*heights[i]
        
        # Find prev smaller element
        #heights=heights[::-1]
        ans2=[0 for i in range(n)]
        left_span=[0 for i in range(n)]
        stk2=[]
        for i in range(n):
            while(stk2 and heights[i]<heights[stk2[-1]]):
                stk2.pop()
            
            if stk2:
                ans2[i]=i-stk2[-1]

            stk2.append(i)
        
        #print("ans2=",ans2)
        for i in range(n):
            if ans2[i]==0:
                left_span[i]=i+1
            else:
                left_span[i]=ans2[i]
        #print("Left_span=",left_span)
        for i in range(n):
            left_result[i]=heights[i]*left_span[i]
        #print("left_result=",left_result)
        for i in range(n):
            final[i]=left_result[i]+right_result[i]-heights[i]
        #print("Right result=",right_result)
        #print("final=",final)
        return max(final)
            

                