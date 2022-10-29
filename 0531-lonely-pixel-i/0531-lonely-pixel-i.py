class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        rows = len(picture)
        cols = len(picture[0])
        
        
        
        horizontals = [row.count('B') for row in picture]
        
        verticals = [[row[i] for row in picture].count('B') for i in range(cols)]
        count = 0
        for r, row in enumerate(picture):
            for i, block in enumerate(row):
                if block == 'W':
                    continue
                else:
                    if verticals[i] == 1 and horizontals[r] == 1:
                        count+=1
        return count