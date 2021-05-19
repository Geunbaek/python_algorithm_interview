class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # solve 1
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        arr = []
        while node.next:
            arr.append(node.val)
            node = node.next
        arr.append(node.val)
        return arr == arr[::-1]

    # solve 2
    def isPalindrome_2(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev




head = ListNode(1, (ListNode(2, ListNode(2, ListNode(1)))))
solution = Solution()
print(solution.isPalindrome(head))
print(solution.isPalindrome_2(head))
