# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            return node




solution = Solution()
solution.buildTree([3,9,20,15,7], [9,3,15,20,7])

"""
Input
[3,9,20,15,7],[9,3,15,20,7]
Output
[3,9,20,null,null,15,7]
"""