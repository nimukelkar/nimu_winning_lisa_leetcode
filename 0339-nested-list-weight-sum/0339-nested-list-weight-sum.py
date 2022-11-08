class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        # self-explanatory DFS recursion
        def dfs(n, d):
            if n.isInteger() : return n.getInteger() * d
            else             : return sum(dfs(i, d+1) for i in n.getList())
            
        return sum(dfs(n, 1) for n in nestedList)