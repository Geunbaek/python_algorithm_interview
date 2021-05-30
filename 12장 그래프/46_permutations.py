from itertools import permutations
class Solution:
    # solve 1
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        prev_elements =[]

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return results
    # solve 2
    def permute_2(self, nums: list[int]) -> list[list[int]]:
        return list(permutations(nums))



solution = Solution()
print(solution.permute([1,2,1]))
"""
Input
[1,2,3]
Output
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""