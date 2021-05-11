from collections import Counter
import re
class Solution:
    # solve 1
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        s = ["!", '?',"'",",",";","."]
        paragraph = paragraph.lower()
        for char in s:
            paragraph = paragraph.replace(char, " ")
        paragraph = paragraph.split()
        for elem in Counter(paragraph).most_common(len(paragraph)):
            if elem[0] not in banned:
                return elem[0]

    # solve 2
    def mostCommonWord_2(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', " ", paragraph).lower().split() if word not in banned]
        return Counter(words).most_common(1)[0][0]




solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(solution.mostCommonWord_2("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

"""
Input
"Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
Output
"ball"
"""