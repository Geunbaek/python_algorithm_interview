class Solution:
    # solve 1
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        for i in range(len(gas)):
            start = i
            total = 0
            ck = True
            for _ in range(len(cost)):
                index = start % len(gas)
                total += gas[index] - cost[index]
                if total < 0:
                    ck = False
                    break
                start += 1
            if ck:
                return i
        return -1

    # solve 2
    def canCompleteCircuit_2(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start






sol = Solution()
print(sol.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))

"""
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
"""