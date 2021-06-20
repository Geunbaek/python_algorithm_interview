class Solution:
    # solve 1
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == target:
                    return True
        return False

    # solve 2
    def searchMatrix_2(self, matrix: list[list[int]], target: int) -> bool:
        return any(target in row for row in matrix)

sol = Solution()
print(sol.searchMatrix([
[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]
], 5))

"""
Input
[
[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]
],  5
Output: true
"""