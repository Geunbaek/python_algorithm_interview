# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        now = parent = ListNode(None)

        while head:
            while now.next and now.next.val < head.val:
                now = now.next

            now.next, head.next, head = head, now.next, head.next

            now = parent
        return now.next

sol = Solution()
print(sol.insertionSortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3))))))

"""
Input: head = [4,2,1,3]
Output: [1,2,3,4]
 
"""