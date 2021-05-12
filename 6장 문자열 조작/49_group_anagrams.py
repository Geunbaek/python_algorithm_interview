from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_dict = defaultdict(list)

        for str in strs:
            str_li = list(str)
            str_li.sort()
            group_dict["".join(str_li)].append(str)

        group_anagram = []
        for val in group_dict.values():
            group_anagram.append(val)
        return group_anagram




solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

"""
Input
["eat","tea","tan","ate","nat","bat"]
Output
[
["bat"],
["nat","tan"],
["ate","eat","tea"]
]
"""