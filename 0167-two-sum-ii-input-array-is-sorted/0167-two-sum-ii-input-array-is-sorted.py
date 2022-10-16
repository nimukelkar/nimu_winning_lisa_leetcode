class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1=0
        ptr2=len(numbers)-1
        l=[]
        
        while(True):
            if numbers[ptr1]+numbers[ptr2]==target:
                return [ptr1+1,ptr2+1]
            if numbers[ptr1]+numbers[ptr2]<target:
                ptr1+=1
            else:
                ptr2-=1
            if ptr1==ptr2:
                break