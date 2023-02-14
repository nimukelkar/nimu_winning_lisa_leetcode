class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        
        
        while(low<=high):
            mid=low+(high-low)//2
            
            sum=0
            for i in range(len(piles)):
                sum+=ceil(piles[i]/mid)
           
            if sum>h:
                low=mid+1
            else:
                high=mid-1
       
        return low