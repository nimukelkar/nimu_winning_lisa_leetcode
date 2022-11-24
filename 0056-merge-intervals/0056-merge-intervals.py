class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        anslist=[]
        
        anslist.append(intervals[0])
        
        prev_start=anslist[-1][0]
        prev_end=anslist[-1][1]
        for i in range(1,len(intervals)):
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]
            
            if curr_start>prev_end:
                #No overlap
                anslist.append(intervals[i])
                prev_start=anslist[-1][0]
                prev_end=anslist[-1][1]
            else:
                #Merge
                anslist[-1][1]=max(anslist[-1][1],intervals[i][1])
                prev_start=anslist[-1][0]
                prev_end=anslist[-1][1]
        return anslist
                                    
                                    
            