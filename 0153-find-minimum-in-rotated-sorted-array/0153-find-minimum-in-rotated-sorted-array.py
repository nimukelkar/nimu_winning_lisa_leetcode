class Solution:
    def findMin(self, nums: List[int]) -> int:
        pole=nums[-1]
        if(len(nums)==1):
            return nums[0]
        low=0
        high=len(nums)-1
        
        while(low<=high):
            mid=low+(high-low)//2
            
            if nums[mid]<pole:
                high=mid-1
            else:
                low=mid+1
        print("low=",low)
        print("high=",high)
        if low<len(nums):
            return nums[low]
        return nums[high]
        