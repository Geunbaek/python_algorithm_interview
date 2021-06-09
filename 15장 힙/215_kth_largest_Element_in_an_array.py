import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, -num)

        for i in range(k-1):
            heapq.heappop(h)
        return heapq.heappop(h)
    # solve 2
    def findKthLargest_2(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(len(nums), nums)[k-1]


solution = Solution()
solution.findKthLargest_2([3,2,1,5,6,4],  2)


"""
Input
[3,2,1,5,6,4],  2
Output: 5
"""




