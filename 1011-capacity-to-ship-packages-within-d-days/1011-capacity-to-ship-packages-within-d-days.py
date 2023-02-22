class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        
        while(low<=high):
            mid=low+(high-low)//2
            
            #Calculate days for cap=mid
            
            count=0
            i=0
            total=0
            while(i<len(weights)):
                total+=weights[i]
                
                if total>mid:
                    count+=1
                    total=0
                    continue
                
                else:
                    i+=1
            
            if count>=days:
                low=mid+1
            else:
                high=mid-1
        
       
        return low