from collections import defaultdict
class Solution:
    # solve 1
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        trace = set()
        visit = set()

        def dfs(i):
            if i in trace:
                return False
            if i in visit:
                return True

            trace.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            trace.remove(i)
            visit.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True

solution = Solution()
solution.canFinish(2, [[1,0]])
solution.canFinish(2, [[1,0],[0,1]])
solution.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])



"""
Input
2, [[1,0]]
Output
true

Input
2, [[1,0],[0,1]]
Output
false

20
[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
"""