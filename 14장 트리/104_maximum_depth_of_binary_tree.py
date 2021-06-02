# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # solve 1
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        results =[]
        def dfs(node, depth):
            if node.left is None and node.right is None:
                results.append(depth)
                return

            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth+1)
        dfs(root, 1)
        return max(results)
    # solve 2
    def maxDepth_2(self, root: TreeNode) -> int:
        if root is None:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth





solution = Solution()
print(solution.maxDepth_2(TreeNode(2, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))))
"""
Input: 
[3,9,20,null,null,15,7]
Output: 3
"""