class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        minutes = 0

        # find all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

        def addOrange(r,c):
            if (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                q.append((r,c))
                grid[r][c] = 2

        # simultaneously bfs through the grid from all rotten oranges
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()

                addOrange(r+1,c)
                addOrange(r-1,c)
                addOrange(r,c-1)
                addOrange(r,c+1)

            if q:
                minutes += 1

        # final lookover to see if there are any fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes