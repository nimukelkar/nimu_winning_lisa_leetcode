class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==i:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j-1],triangle[i-1][j])
        print(triangle)
        return min(triangle[-1])
           
             
                                    
  