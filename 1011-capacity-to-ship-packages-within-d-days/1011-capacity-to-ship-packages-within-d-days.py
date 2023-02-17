class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        weightsum=0
        for i in weights:
            weightsum+=i
        low=max(weights)
        high=weightsum
            
        while(low<=high):
            mid=low+(high-low)//2
            count=0
            i=0
            sum=0
            while(i<len(weights)):
                sum+=weights[i]
                if sum>mid:
                    count+=1
                    sum=0
                    continue
                else:
                    
                    i+=1
            count=count+1
            #print("mid=",mid)
            #print("count=",count)
            
            
            if count>days:
                low=mid+1
            else:
                high=mid-1
            #print("low=",low)
            #print("high=",high)
        print("low=",low)
        print("high=",high)
        return low
                
                