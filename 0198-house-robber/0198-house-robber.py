class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        table=[0]*n
        table[0]=nums[0]
        if n==2:
            table[1]=max(nums[0],nums[1])
            return table[1]
        for i in range(1,n):
            table[i]=max(nums[i]+table[i-2],table[i-1])
        print(table)
        return table[n-1]
            