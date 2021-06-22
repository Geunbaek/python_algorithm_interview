from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        results = []
        window = deque()

        for i in range(len(nums)):

            if window and i - window[0] == k:
                window.popleft()

            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            window.append(i)

            if i + 1 >= k:
                results.append(nums[window[0]])

        return results


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


"""
Input
[1,3,-1,-3,5,3,6,7], 3
Output: [3,3,5,5,6,7]
"""
