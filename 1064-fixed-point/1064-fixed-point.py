class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        low=0
        high=len(arr)-1
        
        while(low<=high):
            mid=low+(high-low)//2
            
            if arr[mid]<mid:
                low=mid+1
            
            else:
                high=mid-1
       
        print("low=",low)
        print("high=",high)
        if low<len(arr) and arr[low]==low:
            return low
        else:
            return -1