# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # solve 1
    def oddEvenList(self, head: ListNode) -> ListNode:
        node = head
        idx = 1
        arr = []
        while node:
            if idx % 2 == 0:
                arr.append(node.val)
                prev.next, node = node.next, prev

            prev, node = node, node.next
            idx += 1
        while arr:
            prev.next = ListNode(arr.pop(0))
            prev = prev.next
        return head

    # solve 1
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head

head = ListNode(1, (ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
solution = Solution()
print(solution.oddEvenList(head))

"""
Input
[1,2,3,4,5]
Output
[1,3,5,2,4]

Input
[2,1,3,5,6,4,7]
Output
[2,3,6,7,1,5,4]
"""