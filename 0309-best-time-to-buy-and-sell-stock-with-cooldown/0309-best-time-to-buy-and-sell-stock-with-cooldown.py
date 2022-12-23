class Solution:
    def maxProfit(self, prices: list[int]) -> int:         # Example: prices = [1,2,3,0,2]
                                                           #
        nostock, stock, cool = 0,-prices[0],0              #   p   nostock   stock    cool 
                                                           #  –––  –––––––  –––––––  –––––––
        for p in prices[1:]:                               #   1      0       -1        0
                                                           #   2      0       -1        1
            nostock, stock, cool = (max(nostock,cool),     #   3      1       -1        2
                                    max(stock,nostock-p),  #   0      2        1       -1
                                    stock+p)               #   2      2        1        3 <––– return
 
        return max(nostock, stock, cool)          
        