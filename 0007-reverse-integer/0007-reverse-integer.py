class Solution:
    def reverse(self, x: int) -> int:
       
        if x>0:
            k= int(str(x)[::-1])
            if k>=(2**31)-1 or k<(-2)**31:
                return 0
            else:
                return k
        else:
            k=int(str(abs(x))[::-1])
            k=k*(-1)
            if k>=(2**31)-1 or k<(-2)**31:
                return 0
            else:
                return k
    