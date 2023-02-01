class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        table=[[0 for i in range(3)]for j in range(n)]
        #print(table)
        if n==1:
            return min(costs[0][0],costs[0][1],costs[0][2])
        for i in range(1):
            for j in range(3):
                table[i][j]=costs[i][j]
        #print(table)
        for i in range(1,n):
            for j in range(3):
                
                    if j==0 and i!=0:
                        table[i][j]=costs[i][j]+min(table[i-1][1],table[i-1][2])
                        
                    elif j==1 and i!=0:
                        table[i][j]=costs[i][j]+min(table[i-1][0],table[i-1][2])
                    elif j==2 and i!=0:
                        table[i][j]=costs[i][j]+min(table[i-1][0],table[i-1][1])
        #print(table)
        return min(table[n-1])