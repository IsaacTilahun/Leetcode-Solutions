class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        state = [0] * numCourses # 0 = not visiting, 1 = visiting
        
        def dfs(crs):
            if state[crs] == 1:
                return False
            if preMap[crs] == []:
                return True

            state[crs] = 1
            for pre in preMap[crs]:
                if not dfs(pre): return False
            state[crs] = 0
            preMap[crs] = []
            return True
        
        # we run through every course IN THE CASE OF DISCONNECTED GRAPHS
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True

        
