class Solution:
    def tribonacci(self, n: int) -> int:
        table=[0 for i in range(n+1)]
        #print(table)
        if n==0:
            return 0
        if n==1:
            table[1]=1
            return 1
        elif n==2:
            table[1]=1
            table[2]=1
            return 1
        
        else:
            table[1]=1
            table[2]=1
            
            for i in range(3,n+1):
                table[i]=table[i-1]+table[i-2]+table[i-3]
            
            return table[n]
                