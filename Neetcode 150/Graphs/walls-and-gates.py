class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        dist = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        def addRoom(r, c):
            if (0 <= r < rows and 0 <= c < cols and grid[r][c] == 2**31 - 1):
                q.append((r,c))
                grid[r][c] = -2 # the -2 essentially is purgatory (just an inf that is about to be set)
                
        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
                
            dist += 1
            