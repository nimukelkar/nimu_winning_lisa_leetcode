class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        l=[]
        def dfs(menu,i,slate):
            if i==n:
                l.append(slate.copy())
                return
            
            for j in range(i,n):
                menu[i],menu[j]=menu[j],menu[i]
                #menu[i] transfer to slate.
                slate.append(menu[i])
                dfs(menu,i+1,slate)
                slate.pop()
                menu[i],menu[j]=menu[j],menu[i]
        dfs(nums,0,[])
        return l
           
                
            
                
                
                