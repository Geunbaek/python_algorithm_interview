class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key = lambda x: ((x[0])**2 + (x[1])**2))
        return points[:k]


sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))
print(sol.kClosest([[3,3],[5,-1],[-2,4]],  2))

"""
Input
[[1,3],[-2,2]], 1
Output: [[-2,2]]

Input
[[3,3],[5,-1],[-2,4]],  2
Output: [[3,3],[-2,4]]
"""