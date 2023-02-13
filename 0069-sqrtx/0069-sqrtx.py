class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x-1
        if x==1 or x==0:
            return x
        while(low<=high):
            mid=low+(high-low)//2
            
            if(x<mid*mid):
                high=mid-1
            else:
                low=mid+1
        print("low=",low)
        print("high=",high)
        return high