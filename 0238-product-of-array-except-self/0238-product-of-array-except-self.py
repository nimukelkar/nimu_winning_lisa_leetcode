class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixprod,suffixprod=1,1
        l1,l2=[],[]
        n=len(nums)
        for i in nums:
            prefixprod*=i
            l1.append(prefixprod)
        
        for i in range(len(nums)-1,-1,-1):
            suffixprod*=nums[i]
            l2.append(suffixprod)
        l2=l2[::-1]
        #print(l1,l2)
        ans=[0]*(n)
        #print(ans)
        
        ans[0]=(l2[1])
        ans[n-1]=l1[n-2]
        for i in range(1,n-1):
            ans[i]=(l2[i+1]*l1[i-1])
        #print(ans)
        return ans
            
        
        