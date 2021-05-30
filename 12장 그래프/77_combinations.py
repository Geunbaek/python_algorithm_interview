from itertools import combinations
class Solution:
    # solve 1
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(combinations([i+1 for i in range(n)], k))

    # solve 2
    def combine_2(self, n: int, k: int) -> list[list[int]]:
        results = []
        prev_elements = []

        def dfs(elements,idx):
            if len(prev_elements) == k:
                results.append(prev_elements[:])

            for i in range(idx, len(elements)):
                prev_elements.append(elements[i])
                dfs(elements, i+1)
                prev_elements.pop()

        dfs([i+1 for i in range(n)], 0)
        return results

solution = Solution()
print(solution.combine_2(4, 2))

"""
Input
4, 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

