class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=[]
        end=[]
     
        global_max=0
        count=0
        
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        
        print(start,end)
        start=sorted(start)
        end=sorted(end)
        ptr1,ptr2=0,0
        count=0
        maxi=0
        n=len(start)
        while(ptr1<=n-1):
            if start[ptr1]<end[ptr2]:
                
                count+=1
                ptr1+=1
                maxi=max(maxi,count)
            else:
                count-=1
                ptr2+=1
               
        return maxi
            