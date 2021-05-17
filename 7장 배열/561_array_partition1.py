class Solution:
    # solve 1
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        for num in nums[::2]:
            sum += num
        return sum

    # solve 2
    def arrayPairSum_2(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])



solution = Solution()
solution.arrayPairSum([1,4,3,2])

"""
Input
[1,4,3,2]
Output
4
"""