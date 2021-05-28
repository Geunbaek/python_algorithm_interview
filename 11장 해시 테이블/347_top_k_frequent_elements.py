from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums).most_common(k)
        result = []
        for val, cnt in freq:
            result.append(val)
        return result


solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))


"""
Input
[1,1,1,2,2,3], 2
Output
[1,2]
"""