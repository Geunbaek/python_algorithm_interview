# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        ans = None
        while node:
            ans, ans.next, node = node, ans, node.next
        return ans



head = ListNode(1, (ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
solution = Solution()
print(solution.reverseList(head))
