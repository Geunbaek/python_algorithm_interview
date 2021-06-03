# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # solve 1
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            if node.left and node.right:
                node.left, node.right = node.right, node.left
            elif node.left:
                node.left, node.right = None, node.left
            elif node.right:
                node.left, node.right = node.right, None

        dfs(root)
        return root

    # solve 2
    def invertTree_2(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree_2(root.right), self.invertTree_2(root.left)
            return root
        return None

