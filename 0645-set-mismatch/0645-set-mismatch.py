class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l=[]
        l2=[]
        for i in range(1,len(nums)+1):
            l.append(i)
        
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>1:
                l2.append(i)
        for i in l:
            if i not in d:
                l2.append(i)
        return l2
        
                
            