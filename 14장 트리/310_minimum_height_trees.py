class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if not edges or len(edges) == 1:
            return [i for i in range(n)]

        graph = [[] for _ in range(n)]
        leaf = []

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        for i in range(len(graph)):
            if len(graph[i]) == 1:
                leaf.append(i)

        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for l in leaf:
                neighbor = graph[l].pop()
                graph[neighbor].remove(l)

                if len(graph[neighbor]) == 1:
                    new_leaf.append(neighbor)
            leaf = new_leaf

        return leaf



solution = Solution()
solution.findMinHeightTrees(6,[[3,0],[3,1],[3,2],[3,4],[5,4]])


"""
Input
6, [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output
[3,4]
"""

