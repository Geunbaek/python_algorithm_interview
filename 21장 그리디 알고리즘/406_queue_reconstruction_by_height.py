import heapq

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        h = []
        ret = []

        for elem in people:
            heapq.heappush(h, (-elem[0], elem[1]))

        while h:
            elem = heapq.heappop(h)
            ret.insert(elem[1], (-elem[0], elem[1]))

        return ret


sol = Solution()
print(sol.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

"""
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
"""