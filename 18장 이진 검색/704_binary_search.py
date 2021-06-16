import bisect
class Solution:
    # solve 1
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return -1
    # solve 2
    def search(self, nums: list[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        return -1





sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9))


"""
Input
[-1,0,3,5,9,12], 9
Output: 4
"""