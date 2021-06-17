class Solution:
    # solve 1
    def search(self, nums: list[int], target: int) -> int:
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append((num, i))
        sorted_nums.sort(key = lambda x:x[0])
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_nums[mid][0] < target:
                left = mid + 1
            elif sorted_nums[mid][0] > target:
                right = mid - 1
            else:
                return sorted_nums[mid][1]
        return -1
    # solve 2
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) -1
        while left < right:
            mid = left + (right - left) //2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) //2
            mid_pivot = (mid+pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))

"""
Input
[4,5,6,7,0,1,2], 0
Output
4
"""
