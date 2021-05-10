class Solution:
    # solve 1
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

    # solve 2
    def reverseString_2(self, s: list[str]) -> None:
        left, right = 0, len(s)-1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

solution = Solution()

s = ["h", "e", "l", "l", "o"]
h = ["H","a","n","n","a","h"]
solution.reverseString(s)
solution.reverseString(h)
print(s)
print(h)

"""
input
["h", "e", "l", "l", "o"]
output
["o", "l", "l", "e", "h"]

Input
["H","a","n","n","a","h"]
Output
["h","a","n","n","a","H"]
"""