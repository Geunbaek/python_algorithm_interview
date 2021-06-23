from collections import Counter

class Solution:
    # solve 1
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]

    # solve 2
    def minWindow_2(self, s: str, t: str) -> str:
        t_cnt = Counter(t)
        current_count = Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        for right, char in enumerate(s, 1):
            current_count[char] += 1

            while current_count & t_cnt == t_cnt:
                if right - left < end - start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1
        return s[start: end] if end - start <= len(s) else ""


sol = Solution()
# print(sol.minWindow("ADOBECODEBANC", "ABC"))
# print(sol.minWindow("a", "a"))
print(sol.minWindow("bbaa", "aba"))


"""
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""
