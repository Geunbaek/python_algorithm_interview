class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums.sort(key = lambda x:str(x)*10, reverse= True)
        ans = ''
        for num in nums:
            ans += str(num)
        return str(int(ans))


sol = Solution()
print(sol.largestNumber([10,2]))
print(sol.largestNumber([3,30,34,5,9]))


"""
Input: nums = [10,2]
Output: "210"

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""