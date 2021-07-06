class Solution:
    # solve 1
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # solve 2
    def fib_2(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x



sol = Solution()
print(sol.fib(2))
print(sol.fib(3))

"""
Input: n = 2
Output: 1

Input: n = 3
Output: 2
"""