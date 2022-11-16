class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        
        count=0
        
        n=len(arr)
        prod=1
        left=0
        count=0
        
        for i in range(n):
            prod=prod*arr[i]
            
            while(left<=i and prod>=k):
                prod=prod//arr[left]
                left+=1
            count+=i-left+1
        return count
                