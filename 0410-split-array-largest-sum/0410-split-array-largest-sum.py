class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=0
        for i in nums:
            high+=i        
        while(low<=high):
            mid=low+(high-low)//2
            
            count=0
            i=0
            sum=0
            while(i<len(nums)):
                sum+=nums[i]
                
                if(sum>mid):
                    count+=1
                    sum=0
                    continue
                
                else:
                    i+=1
            
            if count>=k:
                low=mid+1
            
            else:
                high=mid-1
        
        print("low=",low)
        print("high=",high)
        return low