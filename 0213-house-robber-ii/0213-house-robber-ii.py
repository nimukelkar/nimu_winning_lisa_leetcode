class Solution:
    def rob(self, nums: List[int]) -> int:
        table=[0 for i in range(len(nums))]
        table1=[0 for i in range(len(nums))]
        #print(table)
        n=len(nums)
        if n==1:
            return nums[0]
        
        #Case 1-Rob first house
        table[0]=nums[0]
        
        table[1]=nums[0]
    
        for i in range(2,n-1):
            table[i]=max(nums[i]+table[i-2],table[i-1])
        table[n-1]=table[n-2]
        
        #Case 2-Do not rob 1st house.
        table1[0]=0
        for i in range(1,n):
            if i==1:
                table1[i]=nums[i]
            else:
                table1[i]=max(nums[i]+table1[i-2],table1[i-1])
        return max(table[n-1],table1[n-1])
                
        
            