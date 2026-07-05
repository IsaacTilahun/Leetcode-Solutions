class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]
        state = [0] * n
        result = 0

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node):
            
            if state[node] == 1:
                return

            state[node] = 1

            for neighbor in graph[node]:
                dfs(neighbor)
    
        for i in range(n):
            if state[i] == 0:
                result += 1
            dfs(i)

    
        return result
            

        

        