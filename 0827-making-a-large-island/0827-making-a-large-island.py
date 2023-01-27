class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        v = 2 
        freq = defaultdict(int)
        for r in range(n): 
            for c in range(n): 
                if grid[r][c] == 1: 
                    stack = [(r, c)]
                    grid[r][c] = v
                    while stack: 
                        i, j = stack.pop()
                        freq[v] += 1
                        for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                            if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 1: 
                                stack.append((ii, jj))
                                grid[ii][jj] = v
                    v += 1
                    
        ans = max(freq.values(), default=0)
        for i in range(n): 
            for j in range(n): 
                if grid[i][j] == 0: 
                    cand = 1
                    seen = set()
                    for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                        if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] and grid[ii][jj] not in seen: 
                            seen.add(grid[ii][jj])
                            cand += freq[grid[ii][jj]]
                    ans = max(ans, cand)
        return ans 