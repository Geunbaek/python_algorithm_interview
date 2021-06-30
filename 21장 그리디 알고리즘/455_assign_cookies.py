class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0

        g_left, s_left = 0, 0

        while g_left < len(g) and s_left < len(s):
            if g[g_left] <= s[s_left]:
                cnt += 1
                g_left += 1
                s_left += 1
            else:
                s_left += 1
        return cnt

sol = Solution()
print(sol.findContentChildren(g = [1,2,3], s = [1,1]))
print(sol.findContentChildren(g = [1,2], s = [1,2,3]))

"""
Input: g = [1,2,3], s = [1,1]
Output: 1
Input: g = [1,2], s = [1,2,3]
Output: 2
"""
