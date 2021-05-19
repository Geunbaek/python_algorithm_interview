# Definition for singly-linked list.
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr = []
        l1_now, l2_now = l1, l2

        while l1_now:
            arr.append(l1_now.val)
            l1_now = l1_now.next
        while l2_now:
            arr.append(l2_now.val)
            l2_now = l2_now.next

        arr.sort()
        q = deque(arr)
        if not q:
            return None
        ans = ListNode(q.popleft())
        node = ans
        while q:
            node.next = ListNode(q.popleft())
            node = node.next
        return ans


l1 = ListNode(1, (ListNode(2, ListNode(4))))
l2 = ListNode(1, (ListNode(3, ListNode(4))))
solution = Solution()
print(solution.mergeTwoLists(l1, l2))
