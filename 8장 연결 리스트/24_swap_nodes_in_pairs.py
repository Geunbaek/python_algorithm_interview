# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        node_odd = head
        node_even = head.next

        while node_odd and node_even:
            node_odd.val, node_even.val = node_even.val, node_odd.val
            try:
                node_odd, node_even = node_odd.next.next, node_even.next.next
            except:
                break

        return head


head = ListNode(1, (ListNode(2, ListNode(3, ListNode(4)))))
solution = Solution()
print(solution.swapPairs(head))

"""
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

