# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != 1


        # if len(leaf_depth) == 1:
        #     if leaf_depth[0] <= 1:
        #         return True
        #     else:
        #         return False
        return leaf_depth[-1] - leaf_depth[0] <= 1

solution = Solution()
solution.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
solution.isBalanced(TreeNode(7))
solution.isBalanced(TreeNode(1, TreeNode(2)))
solution.isBalanced(TreeNode(1, None, TreeNode(2, None, TreeNode(3))))
