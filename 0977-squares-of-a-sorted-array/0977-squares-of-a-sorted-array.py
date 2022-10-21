class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ptr1=0
        ptr2=len(nums)-1
        l=[]
        while(True):
            if abs(nums[ptr2])>abs(nums[ptr1]):
                l.append(nums[ptr2]*nums[ptr2])
                ptr2-=1
            else:
                l.append(nums[ptr1]*nums[ptr1])
                ptr1+=1
            if ptr1>ptr2:
                break
        return l[::-1]
            
        