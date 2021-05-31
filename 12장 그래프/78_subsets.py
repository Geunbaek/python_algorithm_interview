from itertools import combinations
class Solution:
    # solve 1
    def subsets(self, nums:list[int]) -> list[list[int]]:
        results = []
        for i in range(len(nums)+1):
            results += list(combinations(nums, i))
        return results

    # solve 2
    def subsets_2(self, nums: list[int]) -> list[list[int]]:
        results = []
        prev_arr = []
        def dfs(idx):
            if idx > len(nums):
                return
            for i in range(idx, len(nums)):
                prev_arr.append(nums[i])
                if prev_arr not in results:
                    results.append(prev_arr[:])
                dfs(i+1)

                prev_arr.pop()
        dfs(0)
        results.append([])
        return results


solution = Solution()
print(solution.subsets_2([1,2,3]))

"""
Input
[1,2,3]
Output
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


