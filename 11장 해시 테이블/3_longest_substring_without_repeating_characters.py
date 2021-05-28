class Solution:
    # solve 1
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        left = 0
        right = 1
        while left <= right and right <= len(s):
            if len(s[left:right]) == len(set(s[left:right])):
                right += 1
            else:
                left += 1
            if len(result) < len(s[left:right - 1]):
                result = s[left:right - 1]
        return len(result)

    # solve 2
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        used = {}
        max_length = start =0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx-start+1)

            used[char] = idx
        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
print(solution.lengthOfLongestSubstring(" "))

"""
Input
"abcabcbb"
Output
3

Input
"bbbbb"
Output
1

Input
"pwwkew"
Output
3

Input
" "
Output
1
"""