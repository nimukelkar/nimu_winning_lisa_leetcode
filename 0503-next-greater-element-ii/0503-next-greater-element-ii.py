class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Monotonic stack
        # 1,2,1-->2,-1,-1 without circular
        # 1,2,1-->2,-1,2
        #1,2,1,1,2,1-->Monotonic stack for 1 pass
        # 1,2,1,1,2,1
        #1-2
        #2--1
        #1
        nums=nums+nums
        stk=[]
        ans=[-1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            
            while(stk and nums[i]>nums[stk[-1]]):
                idx=stk.pop()
                ans[idx]=nums[i]
            stk.append(i)
        return(ans[:len(nums)//2])