class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list]:
        results = []
        prev_elements = []

        def dfs(elements, i):
            if sum(prev_elements) == target:
                results.append(prev_elements[:])
            elif sum(prev_elements) > target:
                return

            for idx in range(i, len(elements)):
                prev_elements.append(elements[idx])
                dfs(elements, idx)
                prev_elements.pop()

        dfs(candidates, 0)
        return results


solution = Solution()
print(solution.combinationSum([2,3,6,7],7))
print(solution.combinationSum([2,3,5], 8))
print(solution.combinationSum([1,2],2))

"""
Input
[2,3,6,7],7
Output
[[2,2,3],[7]]
"""
