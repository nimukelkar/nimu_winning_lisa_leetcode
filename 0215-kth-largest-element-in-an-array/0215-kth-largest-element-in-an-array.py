import random

class Solution:
    def partition(self,nums,low,high):
        i=random.randint(low,high)
        nums[i],nums[low]=nums[low],nums[i]
        ptr1=low+1
        ptr2=high
        while(True):
            if nums[ptr1]<=nums[low]:
                ptr1+=1
                if ptr1>ptr2:
                    break
            if nums[ptr2]>=nums[low]:
                ptr2-=1
                if ptr1>ptr2:
                    break
            if nums[ptr1]>nums[low] and nums[ptr2]<nums[low]:
                nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
                ptr1+=1
                ptr2-=1
                if ptr1>ptr2:
                    break
        nums[ptr2],nums[low]=nums[low],nums[ptr2]
        return ptr2
            
        
        
    def quicksort(self,nums,low,high,ind):
        if low>=high:
            return
        p=self.partition(nums,low,high)
        if p==ind:
            return
        if ind<p:
            self.quicksort(nums,low,p-1,ind)
        else:
            self.quicksort(nums,p+1,high,ind)
        '''p=self.partition(nums,low,high)
        self.quicksort(nums,low,p-1,ind)
        self.quicksort(nums,p+1,high,ind)'''
        return
            
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low=0
        high=len(nums)-1
        self.quicksort(nums,low,high,len(nums)-k)
        #print(nums)
        #print(nums)
        return(nums[len(nums)-k])