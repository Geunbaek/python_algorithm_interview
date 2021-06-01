import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        distance = [float('inf') for _ in range(n+1)]
        h = []
        distance[k] = 0
        times.sort(key = lambda x:x[2])

        for s, e, w in times:
            graph[s].append((w, e))

        for w, e in graph[k]:
            heapq.heappush(h, (w, e))

        while h:
            weight, now = heapq.heappop(h)
            if distance[now] > weight:
                distance[now] = weight
                for w, ne in graph[now]:
                    heapq.heappush(h, (weight+w, ne))

        if float('inf') in distance[1:]:
            return -1
        else:
            return max(distance[1:])

solution = Solution()
solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
solution.networkDelayTime([[1,2,1]], 2,  1)


"""
Input
[[2,1,1],[2,3,1],[3,4,1]], 4, 2

Output
2

Input
[[1,2,1]], 2,  1
Output: 1
"""