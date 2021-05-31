from collections import defaultdict

class Solution:
    # solve 1
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        for a, b in sorted(tickets, reverse= True):
            graph[a].append(b)
        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')

        return route[::-1]
    # solve 2
    def findItinerary_2(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse= True):
            graph[a].append(b)
        stack = ['JFK']
        route = []
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())

        return route[::-1]



solution = Solution()
print(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))


"""
Input
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output
["JFK","ATL","JFK","SFO","ATL","SFO"]
"""