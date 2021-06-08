# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    ret = 0
    # solve 1
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        node = root
        def dfs(node):
            if node is None:
                return
            if low <= node.val <= high:
                self.ret += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(node)
        return self.ret
    # solve 2
    def rangeSumBST_2(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.val > low:
                return dfs(node.right)
            if node.val < high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)

    # solve 3
    def rangeSumBST_3(self, root: TreeNode, low: int, high: int) -> int:
        q, sum = deque([root]), 0
        while q:
            node = q.popleft()
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum




solution = Solution()
print(solution.rangeSumBST(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15))

"""
Input
[10,5,15,3,7,null,18], 7, 15
Output
32
"""
