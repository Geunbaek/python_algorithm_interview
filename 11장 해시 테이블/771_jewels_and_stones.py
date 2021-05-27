from collections import defaultdict, Counter
class Solution:
    # solve 1
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dic = defaultdict(int)
        ret = 0

        for stone in stones:
            if stone in jewels:
                jewels_dic[stone] += 1

        for val in jewels_dic.values():
            ret += val

        return ret

    # solve 2
    def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
        freqs = Counter(stones)
        count = 0

        for char in jewels:
            count += freqs[char]

        return count

    # solve 3
    def numJewelsInStones_3(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)






solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))
print(solution.numJewelsInStones("z","ZZ"))


"""
Input
"aA", "aAAbbbb"
Output
3

Input
"z","ZZ"
Output
0
"""