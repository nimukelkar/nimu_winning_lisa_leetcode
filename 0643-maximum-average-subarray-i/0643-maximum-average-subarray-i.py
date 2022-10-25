class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       
        local_sum=0
        
        for i in range(k):
            local_sum+=nums[i]
        
        maxi=local_sum 
        
        for i in range(k,len(nums)):
                local_sum=local_sum+nums[i]-nums[i-k]
                maxi=max(maxi,local_sum)
               
        return maxi/k