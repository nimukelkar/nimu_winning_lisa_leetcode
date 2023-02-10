class Solution:
    def searchRange(self, a: List[int], target: int) -> List[int]:
        l=[]
        if a==[]:
            return [-1,-1]
        low=0
        high=len(a)-1
        l=[]
        
        while(low<=high):
            mid=low+(high-low)//2
            
            if(a[mid]<target):
                low=mid+1
            else:
                high=mid-1
        print("low=",low)
        if low<len(a) and a[low]==target:
            l.append(low)
        else:
            l.append(-1)
        low=0
        high=len(a)-1
        while(low<=high):
            mid=low+(high-low)//2
            
            if(a[mid]>target):
                high=mid-1
            else:
                low=mid+1
        if a[high]==target:
            
            l.append(high)
        else:
            l.append(-1)
        return l