class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            return 1
       
        
        low=0
        high=n-1
        
        while(low<=high):
            mid=low+(high-low)//2
            
            s=mid*(mid+1)//2
            if s==n:
                return mid
            if s<n:
                low=mid+1
            else:
                high=mid-1
        #print("Low=",low)
        #print("high=",high)
        return high