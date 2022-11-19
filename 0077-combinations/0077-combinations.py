class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        l=[]
        def dfs(menu,i,slate):
            if i==n:
                if len(slate)==k:
                    l.append(slate.copy())
                return
            
            #Take menu[i] and ignore
            dfs(menu,i+1,slate)
            
            #Take menu[i] and append to slate[i]
            slate.append(menu[i])
            dfs(menu,i+1,slate)
            slate.pop()
        
        menu=[]
        for i in range(1,n+1):
            menu.append(i)
        dfs(menu,0,[])
        return l
                        