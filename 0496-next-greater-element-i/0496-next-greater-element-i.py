class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stk=[]
        d={}
        ans=[]
        
        for i in range(len(nums2)):
            
            while(stk and nums2[i]>stk[-1]):
                d[stk[-1]]=nums2[i]
                stk.pop()
            
            stk.append(nums2[i])
        
        
        while stk:
            d[stk[-1]]=-1
            stk.pop()
        
        
        for i in nums1:
            if i in d:
                ans.append(d[i])
        
        return ans
                