class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #Prefixsum
        
        globalcount=0
        n=len(nums)
        prefixsum=0
        d={}
        d[0]=1
        for i in range(n):
            prefixsum+=nums[i]
            #print("prefixsum=",prefixsum)
            
            if prefixsum%k in d:
                globalcount+=d[prefixsum%k]
                d[prefixsum%k]+=1
                
            else:
                d[prefixsum%k]=1
        return globalcount
            