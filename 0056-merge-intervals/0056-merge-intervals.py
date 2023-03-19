class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        ans=[]
        ans.append(intervals[0])
        prev_start=ans[-1][0]
        prev_end=ans[-1][1]
        i=1
        while(i<len(intervals)):
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]
            
            if(curr_start>prev_end):
                #No overlap
                ans.append(intervals[i])
                prev_start=intervals[i][0]
                prev_end=intervals[i][1]
                i+=1
            else:
                #Overlap
                ans[-1][1]=max(ans[-1][1],curr_end)
                prev_start=ans[-1][0]
                prev_end=ans[-1][1]
                i+=1
        return ans
                                
            