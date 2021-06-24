from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        counts = Counter()
        left, right = 0, 0

        for right in range(1, len(s)+1):
            counts[s[right - 1]] += 1

            max_char_n = counts.most_common(1)[0][1]
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return right - left





sol = Solution()
print(sol.characterReplacement(s = "ABAB", k = 2))

"""
Input: s = "ABAB", k = 2
Output: 4

Input: s = "AABABBA", k = 1
Output: 4
"""