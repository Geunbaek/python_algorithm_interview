# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        arr = ['#']
        while q:
            node = q.popleft()
            if node is not None:
                q.append(node.left)
                q.append(node.right)
                arr.append(str(node.val))
            if node is None:
                arr.append('#')
        return ' '.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None
        data = data.split()
        root = TreeNode(data[1])
        index = 2
        q = deque(root)
        while q:
            node = q.popleft()
            if node.left is not None:
                node.left = TreeNode(data[index])
                q.append(node.left)
            index += 1
            if node.right is not None:
                node.right = TreeNode(data[index])
                q.append(node.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
print(ser.serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))
# ans = deser.deserialize(ser.serialize(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))))