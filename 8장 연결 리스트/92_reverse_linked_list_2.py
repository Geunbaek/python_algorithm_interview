# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next

        for _ in range(right-left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
# print(solution.reverseBetween(head,2, 4))
head = ListNode(3, (ListNode(5)))
print(solution.reverseBetween(head, 1, 2))


"""
Input 
[1,2,3,4,5], 2, 4
Output
[1,4,3,2,5]

[3,5]
1
2
"""