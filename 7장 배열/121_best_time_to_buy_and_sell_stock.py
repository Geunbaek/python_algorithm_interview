class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_val = 10**8
        max_profit = 0

        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)

        return max_profit

solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))

"""
Input
[7,1,5,3,6,4]
Output
5
"""