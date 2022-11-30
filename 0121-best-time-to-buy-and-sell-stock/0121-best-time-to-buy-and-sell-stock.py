class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        table=[0]*(n)
        table[0]=0
        mini=float("inf")
        
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            
            table[i]=max(prices[i]-mini,table[i-1])
        return max(table)