class Solution(object):
    def sortColors(self, nums):
        d={0:0,1:0,2:0}
        l=[]
        
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        #print(d)
        
        for i in d:
            for k in range(d[i]):
                l.append(i)
                #print("l=",l)
        for i in range(len(nums)):
            nums[i]=l[i]
        return nums
        