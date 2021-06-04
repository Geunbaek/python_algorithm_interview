# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else:

            return root1 or root2


solution = Solution()
print(solution.mergeTrees(TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2)), TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))))

"""
Input
[1,3,2,5], [2,1,3,null,4,null,7]
Output
[3,4,5,5,4,null,7]
"""