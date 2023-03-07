class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        #Very similar to package D boxes.
    
        low=1
        high=1000000000000000000000
        
        while(low<=high):
            mid=low+(high-low)//2
            
            #Calculate trips for t=mid
            count=0
            for i in range(len(time)):
                count+=mid//time[i]
            #print("count=",count)
            if count>=totalTrips:
                #Push to right
                high=mid-1
            
            else:
                low=mid+1
        
        #print("low=",low)
        #print("high=",high)
        return low