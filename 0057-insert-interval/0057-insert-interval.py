class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals=sorted(intervals,key=lambda x:x[0])
        
        #print(intervals)
        
        anslist=[]
        anslist.append(intervals[0])
        prev_start=anslist[-1][0]
        prev_end=anslist[-1][1]
        
        
        for i in range(1,len(intervals)):
            curr_start=intervals[i][0]
            curr_end=intervals[i][1]
            
            if curr_start>prev_end:
                #Append to anslist
                anslist.append(intervals[i])
                prev_start=intervals[i][0]
                prev_end=intervals[i][1]
            else:
                #Merge into anslist
                anslist[-1][1]=max(anslist[-1][1],curr_end)
                prev_start=anslist[-1][0]
                prev_end=anslist[-1][1]
        return anslist
                                  