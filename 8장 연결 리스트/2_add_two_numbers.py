# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_node, l2_node = l1, l2
        l1_val, l2_val = [], []
        while l1_node:
            l1_val.append(str(l1_node.val))
            l1_node = l1_node.next
        while l2_node:
            l2_val.append(str(l2_node.val))
            l2_node = l2_node.next

        sum_val = list(str(int("".join(l1_val[::-1])) + int("".join(l2_val[::-1]))))
        ans = ListNode(sum_val.pop(0))
        ans_node = ans
        while sum_val:
            ans_node.next = ListNode(sum_val.pop(0))
            ans_node = ans_node.next

        return ans






l1 = ListNode(2, (ListNode(4, ListNode(3))))
l2 = ListNode(5, (ListNode(6, ListNode(4))))
solution = Solution()
print(solution.addTwoNumbers(l1, l2))

"""
Input 
l1 = [2,4,3], l2 = [5,6,4]
Output
[7,0,8]
"""

