class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        local_sum=0
        count=0
        
        for i in range(k):
            local_sum+=arr[i]
       
        if local_sum/k>=threshold:
            count+=1
            
        for i in range(k,len(arr)):
            local_sum=local_sum+arr[i]-arr[i-k]
            if local_sum/k>=threshold:
                count+=1
        return count