# My solution

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(current):
            if current[-1] == len(graph)-1:
                ans.append(current)
                return
            
            for n in graph[current[-1]]:
                dfs(current+[n])
                
        ans = []
        dfs([0])
        return ans
