# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sum_val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.right)
                self.sum_val += node.val
                node.val = self.sum_val
                dfs(node.left)

        dfs(root)
        return root





solution = Solution()
print(solution.bstToGst(TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))))


"""
Input
[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output
[30,36,21,36,35,26,15,null,null,null
"""
