class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1=0
        ptr2=len(numbers)-1
        l=[]
        while(ptr1<ptr2):
            if numbers[ptr1]+numbers[ptr2]==target:
                l.append(ptr1+1)
                l.append(ptr2+1)
                return l
            elif numbers[ptr1]+numbers[ptr2]>target:
                ptr2-=1
            else:
                ptr1+=1
                
                