from itertools import product

class Solution:
    # solve 1
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        number_char = {"2": ['a','b','c'],
                       "3":['d','e','f'],
                       '4': ['g','h','i'],
                       '5':['j','k','l'],
                       '6':['m','n','o'],
                       '7':['p','q','r','s'],
                       '8':['t','u','v'],
                       '9':['w','x','y','z']
                       }
        digit_arr, result = [], []
        for digit in digits:
            digit_arr.append(number_char[digit])
        for elem in list(product(*digit_arr)):
            result.append(''.join(elem))
        return result
    # solve 2
    def letterCombinations_2(self, digits: str) -> list[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for char in number_char[digits[index]]:
                dfs(index + 1, path + char)
        if not digits:
            return []

        result = []
        number_char = {"2": ['a', 'b', 'c'],
                       "3": ['d', 'e', 'f'],
                       '4': ['g', 'h', 'i'],
                       '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'],
                       '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'],
                       '9': ['w', 'x', 'y', 'z']
                       }
        dfs(0, "")
        return result


solution = Solution()
solution.letterCombinations("23")
solution.letterCombinations_2("23")

"""
Input
"23"
Output
["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""