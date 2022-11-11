class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        d={}
        stack=[]
        l=[]
        for i in range(n):
        
            while (stack and nums2[i]>stack[-1]):
                #Make a match.
                d[stack[-1]]=nums2[i]
                stack.pop()

            stack.append(nums2[i])

        #print("stack=",stack)
        while(stack):
            d[stack[-1]]=-1
            stack.pop()
        #print(d)
        for i in nums1:
            l.append(d[i])
        return l