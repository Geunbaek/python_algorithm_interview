from collections import deque
import re

class Solution:
    # solve 1
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char.lower())
        if arr == arr[::-1]:
            return True
        return False

    # solve 2
    def isPalindrome_2(self, s: str) -> bool:
        arr = deque()
        for char in s:
            if char.isalnum():
                arr.append(char.lower())

        while len(arr) > 1:
            if arr.popleft() != arr.pop():
                return False
        return True
    # solve 3
    def isPalindrome_3(self, s: str) -> bool:
        s = re.sub("[^0-9a-zA-Z]","", s)
        s = s.lower()
        return s == s[::-1]



solution = Solution()
solution.isPalindrome("A man, a plan, a canal: Panama")
solution.isPalindrome("race a car")

"""
input
"A man, a plan, a canal: Panama"
output
true

input
"race a car"
output
false
"""