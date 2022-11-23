class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        l=[]
        
        def dfs(menu,i,slate):
            if i==n:
                l.append(slate.copy())
                return
            
            s=set()
            for j in range(i,n):
                if menu[j] not in s:
                    s.add(menu[j])
                    menu[j],menu[i]=menu[i],menu[j]
                    slate.append(menu[i])
                    dfs(menu,i+1,slate)
                    slate.pop()
                    menu[j],menu[i]=menu[i],menu[j]
        dfs(nums,0,[])
        return l
           
                