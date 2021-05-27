# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # solve1
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        elements = []
        for head in lists:
            node = head
            while node:
                elements.append(node.val)
                node= node.next
        elements.sort(reverse=True)
        if not elements:
            return None
        head = ListNode(elements.pop())
        node = head
        while elements:
            node.next = ListNode(elements.pop())
            node = node.next
        return head

    # solve2
    def mergeKLists_2(self, lists: list[ListNode]) -> ListNode:
        root = result = ListNode(None)
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))

        while h:
            node = heapq.heappop(h)
            idx = node[1]
            result.next = node[2]

            result = result.next

            if result.next:
                heapq.heappush(h, (result.next.val, idx, result.next))
        return root.next

solution = Solution()
solution.mergeKLists([
                    ListNode(1, ListNode(4, ListNode(5))),
                    ListNode(1, ListNode(3, ListNode(4))),
                    ListNode(2, ListNode(6))
                    ])


"""
Input
[
  1->4->5,
  1->3->4,
  2->6
]
Output
1->1->2->3->4->4->5->6
"""