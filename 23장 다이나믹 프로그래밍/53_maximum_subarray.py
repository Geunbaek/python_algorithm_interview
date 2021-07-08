import sys

class Solution:
    # solve 1
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i - 1] > 0 else 0
        return max(nums)

    # solve 2
    def maxSubArray_2(self, nums: list[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum



sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
"""