class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        l=sorted(intervals,key=lambda x:x[1])
        print(l)
        
        for i in range(len(l)-1):
            if l[i][1]>l[i+1][0]:
                return False
        return True