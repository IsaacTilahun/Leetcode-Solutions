class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) not in visit and 0 <= r < rows and 0 <= c < cols and heights[r][c] >= prevHeight):
                visit.add((r,c))
                dfs(r-1, c, visit, heights[r][c])
                dfs(r+1, c, visit, heights[r][c])
                dfs(r, c-1, visit, heights[r][c])
                dfs(r, c+1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        return [[r,c] for r,c in pacific.intersection(atlantic)]




        
        
            






        


        