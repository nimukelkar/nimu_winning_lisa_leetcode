class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums=sorted(nums)
        for i in range(len(nums)-2):
            ptr1=i+1
            ptr2=len(nums)-1
            
            a=nums[i]
            
            while(True):
                if a+nums[ptr1]+nums[ptr2]==0:
                    if [a,nums[ptr1],nums[ptr2]] not in l:
                        l.append([a,nums[ptr1],nums[ptr2]])
                if a+nums[ptr1]+nums[ptr2]<=0:
                    ptr1+=1
                else:
                    ptr2-=1
                if ptr1==ptr2:
                    break
        return l
                    
            