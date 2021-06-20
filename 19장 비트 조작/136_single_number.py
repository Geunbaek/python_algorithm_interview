class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = nums[0]
        for num in nums[1:]:
            result ^= num

        return result


sol = Solution()
print(sol.singleNumber([2,2,1]))

"""
Input: nums = [2,2,1]
Output: 1
"""
