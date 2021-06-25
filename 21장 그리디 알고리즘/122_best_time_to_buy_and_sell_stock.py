class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ret = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                ret += prices[i] - prices[i-1]
        return ret




sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))


"""
Input: prices = [7,1,5,3,6,4]
Output: 7
"""
