class Solution:
    # solve 1
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    if (nums[i], nums[left], nums[right]) not in result:
                        result.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -=1

        return result

    # solve 2
    def threeSum_2(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -=1

        return result



solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
print(solution.threeSum_2([-1,0,1,2,-1,-4]))
"""
Input
[-1,0,1,2,-1,-4]
Output
[[-1,-1,2],[-1,0,1]]
"""