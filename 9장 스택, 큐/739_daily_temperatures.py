from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list:
        stack = []
        tmp = []
        ans = [0 for _ in range(len(temperatures))]
        for idx, temperature in enumerate(temperatures):
            tmp.append((idx, temperature))
        temperatures = deque(tmp)
        while temperatures:
            if not stack:
                stack.append(temperatures.popleft())
            while stack and temperatures and stack[-1][1] >= temperatures[0][1]:
                stack.append(temperatures.popleft())
            while stack and temperatures and stack[-1][1] < temperatures[0][1]:
                elem = stack.pop()
                ans[elem[0]] = temperatures[0][0] - elem[0]
        return ans

    def dailyTemperatures_2(self, temperatures: list[int]) -> list:
        answer = [0] * len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer


solution = Solution()
# print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(solution.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))


"""
input
[73, 74, 75, 71, 69, 72, 76, 73]
output
[1, 1, 4, 2, 1, 1, 0, 0]
"""