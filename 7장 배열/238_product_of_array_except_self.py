class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out = []
        p = 1
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out

solution = Solution()
solution.productExceptSelf([1,2,3,4])

"""
Input
[1,2,3,4]
Output
[24,12,8,6]
"""
