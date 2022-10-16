class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)-1
        mid=(low+high)//2
        self.quicksort(nums,low,high)
        return nums
    
    
    def partition(self,nums,low,high):
        temp=random.randint(low,high)
        nums[temp],nums[low]=nums[low],nums[temp]
        
        pindex=low
        ptr2=high
        curr=pindex+1
        
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
        #print(nums)
        return ptr2
    def quicksort(self,arr,low,high):
        if (low >= high):
            return
        p=self.partition(arr,low,high)
        self.quicksort(arr,low,p-1)
        self.quicksort(arr,p+1,high)
