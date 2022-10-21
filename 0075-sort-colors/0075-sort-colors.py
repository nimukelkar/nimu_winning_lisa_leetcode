
class Solution:
    def partition(self,nums,low,high):
        piv=nums[0]
        pindex=low
        ptr1=low+1
        ptr2=high
        while(True):
            if nums[ptr1]<nums[pindex]:
                ptr1+=1
                if ptr1>ptr2:
                    break
            
            else:
                nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
                ptr2-=1
                if ptr1>ptr2:
                    break
            
        nums[ptr2],nums[pindex]=nums[pindex],nums[ptr2]
        return ptr2
    
    def quicksort(self,nums,low,high):
        mid=(low+high)//2
        if(low>=high):
            return
        p=self.partition(nums,low,high)
        self.quicksort(nums,low,p-1)
        self.quicksort(nums,p+1,high)
    def sortColors(self, nums: List[int]) -> None:
        low=0
        high=len(nums)-1
        self.quicksort(nums,low,high)
        return nums