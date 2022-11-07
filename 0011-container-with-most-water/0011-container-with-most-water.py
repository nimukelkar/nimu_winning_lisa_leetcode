class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        
        ptr1=0
        ptr2=len(height)-1
        
        while(ptr1<ptr2):
            area=min(height[ptr2],height[ptr1])*(ptr2-ptr1)
            max_area=max(area,max_area)
            
            if height[ptr1]<=height[ptr2]:
                ptr1+=1
            else:
                ptr2-=1
        return max_area