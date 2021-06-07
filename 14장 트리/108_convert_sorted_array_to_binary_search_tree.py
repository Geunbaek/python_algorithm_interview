# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def dfs(arr):
            if not arr:
                return
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            left = arr[:mid]
            right = arr[mid+1:]
            node.left = dfs(left)
            node.right = dfs(right)
            return node

        return dfs(nums)



solution = Solution()
print(solution.sortedArrayToBST([-10,-3,0,5,9]))

"""
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
"""