class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(r,c):
            if (0 <= r < rows and 0 <= c < cols and (r,c) not in visited and board[r][c] == "O"):
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c] == "O":
                dfs(rows-1, c)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1] == "O":
                dfs(r, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

        