class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n,k=len(costs),len(costs[0])
        table=[[0 for i in range(k)]for j in range(n)]
        #print(table)
        
        table[0]=costs[0]
        #print(table)
        
        
        if len(costs)==1:
            return min(table[0])
        
        else:
            for i in range(1,n):
                
                for j in range(k):
                    mini=float("inf")
                    for m in range(j+1,k):
                        #print('Hi')
                        #print("costs[i][m]",costs[i][m])
                        if mini>table[i-1][m]:
                            #print("In here")
                            mini=table[i-1][m]
                    for m in range(0,j):
                        if mini>table[i-1][m]:
                            mini=table[i-1][m]
                    table[i][j]=mini+costs[i][j]
        print(table)
        return min(table[n-1])