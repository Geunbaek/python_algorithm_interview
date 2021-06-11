class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        intervals.sort(key = lambda x:x[0])
        for i in intervals:
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged


solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))

"""
Input
[[1,3],[2,6],[8,10],[15,18]]
Output
[[1,6],[8,10],[15,18]]
"""