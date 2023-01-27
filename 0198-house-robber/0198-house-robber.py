class Solution:
    def rob(self, nums: List[int]) -> int:
        table=[0 for i in range(len(nums)+1)]
        l=len(nums)
        if l==1:
            table[0]=nums[0]
            return table[0]
        elif l==2:
            
            table[1]=max(nums[0],nums[1])
            return table[1]
        
        else:
            table[0]=nums[0]
            table[1]=max(nums[0],nums[1])
            
            for i in range(2,len(nums)):
                table[i]=max(nums[i]+table[i-2],table[i-1])
            
            return table[l-1]
                
            
        