class Solution:
    # solve 1
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    # solve 2
    def sortColors_2(self, nums: list[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1





sol = Solution()
arr = [2,0,2,1,1,0]
sol.sortColors_2(arr)
print(arr)
"""
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


