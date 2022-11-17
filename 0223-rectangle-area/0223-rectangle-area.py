class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        area_1 = (ax2 - ax1) * (ay2 - ay1)               # [1] area of the first rectangle
        area_2 = (bx2 - bx1) * (by2 - by1)               # [2] area of the second rectangle 
        x_over = max(min(ax2,bx2) - max(ax1,bx1),0)      # [3] overlap of sides along x-axis
        y_over = max(min(ay2,by2) - max(ay1,by1),0)      # [4] overlap of sides along y-axis
        area_0 = x_over * y_over                         # [5] area of the overlap region
        
        return area_1 + area_2 - area_0