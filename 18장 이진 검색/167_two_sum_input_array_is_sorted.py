class Solution:
    # solve 1
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[i] + numbers[mid] < target:
                    left = mid + 1
                elif numbers[i] + numbers[mid] > target:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]
    # solve 2
    def twoSum_2(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) -1
        while left != right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]





sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([2,3,4], 6))

"""
Input
[2,7,11,15], 9
Output: [1,2]

Input
[2,3,4], 6
Output: [1,3]

Input
[-1,0], -1
Output: [1,2]
"""