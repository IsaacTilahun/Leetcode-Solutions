class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        state = [0] * numCourses # 0 nothing, 1 in visitation, 2 done
        order = []

        def dfs(crs):
            
            # Loop Check
            if state[crs] == 1:
                return False

            # If Done Already
            elif state[crs] == 2:
                return True
            
            state[crs] = 1
            
            for pre in graph[crs]:
                if not dfs(pre): return False

            state[crs] = 2
            order.append(crs)
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return order