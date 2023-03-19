class Solution:
    def partition(self,nums,low,high):
        r=random.randint(low,high)
        nums[low],nums[r]=nums[r],nums[low]
        pindex=low
        curr=pindex+1
        ptr2=high
        while(True):
            if nums[curr]<=nums[pindex]:
                curr+=1
                if curr>ptr2:
                    break
            if nums[curr]>=nums[pindex]:
                nums[curr],nums[ptr2]=nums[ptr2],nums[curr]
                ptr2-=1
                if curr>ptr2:
                    break
        nums[pindex],nums[ptr2]=nums[ptr2],nums[pindex]
        return ptr2
    
    def quicksort(self,nums,low,high):
        if low>=high:
            return
        p=self.partition(nums,low,high)
        self.quicksort(nums,low,p-1)
        self.quicksort(nums,p+1,high)
    
    
    
    def sortArray(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)-1
        
        self.quicksort(nums,low,high)
        return nums
    
    
    
    
    
    
    
        