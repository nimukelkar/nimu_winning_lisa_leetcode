class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])
        #print(n)
        l=[]
        def dfs(menu,i,slate):
            
            if i==n:
                l.append("".join(slate.copy()))
                return
            
            
            for j in range(2):
                slate.append(menu[j])
                dfs(menu,i+1,slate)
                slate.pop()
            return
        menu=["0","1"]
        dfs(menu,0,[])
        for i in l:
            if i not in nums:
                return i
                    
                