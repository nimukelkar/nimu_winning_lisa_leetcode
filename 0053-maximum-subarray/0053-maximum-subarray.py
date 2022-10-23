class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        table=[0]*(n)
        table[0]=nums[0]
        for i in range(1,n):
            table[i]=max(nums[i],nums[i]+table[i-1])
        return max(table)