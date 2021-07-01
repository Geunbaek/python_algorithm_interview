from collections import Counter

class Solution:
    # solve 1
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]

    # solve 2
    def majorityElement_2(self, nums: list[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2
        a = self.majorityElement_2(nums[:mid])
        b = self.majorityElement_2(nums[mid:])

        return [b, a][nums.count(a) > len(nums)//2]


sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement_2([3,2,3]))

"""
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
