from collections import Counter
class Solution:
    # solve 1
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ""

    # solve 2
    def removeDuplicateLetters_2(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []
        for char in s:
            print(stack, seen)
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)



solution = Solution()
print(solution.removeDuplicateLetters_2("bcabc"))


"""
Input
"bcabc"
Output
"abc"
"""