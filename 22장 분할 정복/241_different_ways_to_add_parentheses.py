class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def calc(left, right, op):
            ret = []

            for l in left:
                for r in right:
                    ret.append(eval(str(l) + op + str(r)))

            return ret

        if expression.isdigit():
            return [int(expression)]

        results = []

        for index, elem in enumerate(expression):
            if elem in '+-*':
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(calc(left, right, elem))

        return results


sol = Solution()

print(sol.diffWaysToCompute("2-1-1"))
print(sol.diffWaysToCompute("2*3-4*5"))

"""
Input: expression = "2-1-1"
Output: [0,2]

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
"""
