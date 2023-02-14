class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        k=(int(a,2))
        l=(int(b,2))
        m=k+l
        return bin(m).replace("0b","")