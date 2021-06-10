from collections import defaultdict

class Node:
    def __init__(self):
        self.word = -1
        self.child = defaultdict(Node)
        self.palindrome = []

class Trie:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    def insert(self, word , idx):
        node = self.root
        for i, char in enumerate(word[::-1]):
            if self.is_palindrome(word[:len(word)-i]):
                node.palindrome.append(idx)
            node = node.child[char]
        node.word = idx

    def search_pal(self, word, idx):
        result = []
        node = self.root

        while word:
            if node.word >= 0:
                if self.is_palindrome(word):
                    result.append([idx, node.word])
            if not word[0] in node.child:
                return result
            node = node.child[word[0]]
            word = word[1:]

        if node.word >= 0 and node.word != idx:
            result.append([idx, node.word])
        for palindrome_word in node.palindrome:
            result.append([idx, palindrome_word])
        return result



class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        trie = Trie()
        results = []
        for i, word in enumerate(words):
            trie.insert(word, i)

        for i, word in enumerate(words):
            results.extend(trie.search_pal(word, i))
        return results




sol = Solution()
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))

"""
Input
["abcd","dcba","lls","s","sssll"]
Output
[[0,1],[1,0],[3,2],[2,4]]
"""