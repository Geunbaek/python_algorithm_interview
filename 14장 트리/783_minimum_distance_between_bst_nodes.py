# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import sys
class Solution:
    # solve 1
    def minDiffInBST(self, root: TreeNode) -> int:
        values = []
        ret = 10**9
        def dfs(node):
            if node:
                values.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        dfs(root)
        values.sort()
        for val1, val2 in zip(values, values[1:]):
            ret = min(ret, val2-val1)
        return ret

    # solve 2
    def minDiffInBST_2(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result = min(result, node.val - prev)
            prev = node.val

            node = node.right
        return result

solution = Solution()
print(solution.minDiffInBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))))

"""
Input: 
[4,2,6,1,3]
Output: 1
"""
