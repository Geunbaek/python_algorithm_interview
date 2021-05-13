class Solution:
    # solve 1
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx in range(len(nums)):
            for idx2 in range(idx+1, len(nums)):
                if nums[idx] + nums[idx2] == target:
                    return [idx, idx2]

    # solve 2
    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i+1)

    # solve 3
    def twoSum_3(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            num_map[num] = i

        for i, num in enumerate(nums):
            if target - num in num_map and i != num_map[target-num]:
                return i, num_map[target - num]


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum_2([2,7,11,15], 9))
print(solution.twoSum_3([2,7,11,15], 9))

"""
Input
[2,7,11,15], 9
Output 
[0,1]

"""