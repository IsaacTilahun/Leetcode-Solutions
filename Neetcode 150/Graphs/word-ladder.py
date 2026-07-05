class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                graph[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        result = 1

        while q:
            """
            Remember len(q) is stuck in time, allowing for BFS to be tracked layer-by-layer.
            Also note how we somewhat built a graph inside of the BFS. We had a graph that tracked
            wildcards (e.g. h*t) to words like hot or hit, but we used that to see what would be
            a neighbor of hot itself (in some supposed new graph), AS we were doing BFS.
            """
            for i in range(len(q)): 
                word = q.popleft() 
                if word == endWord:
                    return result
                
                # now we need to find the neighbors
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in graph[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
                    graph[pattern] = []
            result += 1

        return 0

        




        


"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        graph = {}
        visited = set()
        graph[beginWord] = []

        def bfs(word) -> int:
            
            q = collections.deque()
            q.append(word)
            visited.add(word)
            result = 1

            while q:
                w = q.popleft()

                for neighbor in graph[w]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    q.append(neighbor)
                    result += 1
                    if neighbor == endWord:
                        return result
            return 0


        # checks if 2 words have a one letter difference
        def oneLetterDiff(word1, word2):
            diffNum = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    diffNum += 1
                    if diffNum == 2:
                        return False
            return diffNum == 1

        # creates graph as needed
        for i in wordList:
            if oneLetterDiff(beginWord, i):
                graph[beginWord].append(i)
            graph[i] = []
            for j in wordList:
                if oneLetterDiff(i, j):
                    graph[i].append(j)
        
        return bfs(beginWord)
"""