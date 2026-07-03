class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]
        visited = set()

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, prev):
            
            # If already visited; loop
            if node in visited:
                return False
            
            visited.add(node)
            for n in graph[node]:
                if n != prev:
                    if not dfs(n, node): return False
            return True

        return (dfs(0, -1) and len(visited) == n)

