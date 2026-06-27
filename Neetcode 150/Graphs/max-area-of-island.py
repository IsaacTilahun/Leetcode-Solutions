class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        maxarea = 0

        def dfs(r, c):
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            area = 1

            return area + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(i, j))
        return maxarea
