class Solution:
    # solve 1
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == "{" or char == '[':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False
            elif char == '}':
                if not stack:
                    return False
                if stack.pop() != '{':
                    return False
            elif char == ']':
                if not stack:
                    return False
                if stack.pop() != '[':
                    return False
        if stack:
            return False

        return True

    # solve 2
    def isValid_2(self, s: str) -> bool:
        stack = []
        table = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack and table[char] != stack.pop():
                return False
        return len(stack) == 0


solution = Solution()
print(solution.isValid("()[]{}"))
"""    
Input 
"()[]{}"
Output 
true
"""

