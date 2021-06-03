# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    longest = 0
    # solve 1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right + 2)

            return max(left, right) + 1
        dfs(root)
        return self.longest


solution = Solution()
print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2))))


"""
Input
[1,2,3,4,5]
Output
3
"""
