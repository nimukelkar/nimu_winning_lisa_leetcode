class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        print("m=",m,"n=",n)
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i-1][j-1]!=matrix[i][j]:
                    return False
        return True
                