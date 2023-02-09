class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        flag=0
        
        while(low<=high):
            mid=(low+high)//2
            
            if(nums[mid]==target):
                flag=1
                return mid
            elif nums[mid]>target:
                high=mid-1
            
            else:
                low=mid+1
        if flag==0:
            if target>nums[len(nums)-1]:
                return len(nums)
            elif target<nums[0]:
                return 0
            for i in range(len(nums)-1):
                if nums[i]<target and nums[i+1]>target:
                    return i+1
        
        