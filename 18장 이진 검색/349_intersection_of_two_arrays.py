class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        return nums1 & nums2


sol = Solution()
print(sol.intersection([1,2,2,1],[2,2]))

"""
Input
[1,2,2,1],[2,2]
Output: [2]
"""