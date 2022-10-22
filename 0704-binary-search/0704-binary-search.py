class Solution:
    def search(self, a: List[int], target: int) -> int:
        low=0
        high=len(a)-1
        
        while(True):
            mid=(low+high)//2
            if a[mid]==target:
                return mid
            if a[mid]<target:
                low=mid+1
            else:
                high=mid-1
            if low>high:
                return -1