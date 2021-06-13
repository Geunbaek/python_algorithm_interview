class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


sol = Solution()
print(sol.isAnagram())


"""
Input: s = "anagram", t = "nagaram"
Output: true
"""
